from datetime import date
from datetime import datetime
from helpers.history_fetcher import HistoryFetcher
import dateutil.parser
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import json
import folium

# returns the estimated wikipedia page stability from year_start to November 2017 (now).
# The bigger the outlier factor, the more events are ignored (should be between 2 and 100)
# can plot analytical data
def wiki_change_factor(wiki_name,year_start, outlier_factor, plot_on = False):

    # fetch the changes
    history_fetcher = HistoryFetcher(wiki_name)
    response = history_fetcher.get_history(str(year_start)+'0101000000', '20171128000000')
    dates = list(map(lambda revision: revision['timestamp'], response))
    dates_pd = pd.DataFrame(dates, columns=['date'])
    dates_pd['change']= 1;

    # aggregate per month
    changes_aggregated_month = np.zeros([(2017 - year_start)*12,1])
    date_last = date(year=year_start,month=11,day=1)
    for y in range(year_start,2017):
        for m in range(0,12):
            date_current = date(year=y,month=m+1,day=1)
            changes_month = np.sum(dates_pd[ dates_pd['date'] > date_last][ dates_pd['date'] < date_current]['change'])
            changes_aggregated_month[-1+m+(y-year_start)*12]=changes_month
            date_last = date_current

    changes_aggregated_month = np.squeeze(changes_aggregated_month)

    thr_val = outlier_factor * np.mean(changes_aggregated_month)
    thr2_val = thr_val*0.7

    if(plot_on):
        plt.rcParams["figure.figsize"] = (7,7)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.bar(range(len(changes_aggregated_month)), changes_aggregated_month)
        plt.title('Wiki changes/month for ' + wiki_name + ' from ' + str(year_start) + ' till now')
        plt.axhline(thr_val, color="grey")
        plt.xlabel('months from '+ str(year_start) + ' till now')
        plt.ylabel('aggregated changes/month')

        indices = [i for i,v in enumerate(changes_aggregated_month >= thr_val) if v]
        plt.bar(indices, changes_aggregated_month[indices],color='red')
        plt.text(1.02,thr_val, 'summed as extrordinary\n changes above this line', va='center', ha="left", bbox=dict(facecolor="w",alpha=0.5),
        transform=ax.get_yaxis_transform())
        indices2 = [i for i,v in enumerate( (changes_aggregated_month >= thr2_val) & (changes_aggregated_month < thr_val)) if v]
        plt.bar(indices2, changes_aggregated_month[indices2],color='orange')
        plt.text(1.02,thr2_val, 'significant above avg\n changes above this line', va='center', ha="left", bbox=dict(facecolor="w",alpha=0.5),
        transform=ax.get_yaxis_transform())
        plt.axhline(thr2_val, color="grey")
        plt.show()

     # select outliers
    sum_outliers = np.sum(changes_aggregated_month[changes_aggregated_month > thr_val])
    sum_outliers += 0.2 * np.sum(changes_aggregated_month[ (changes_aggregated_month >= thr2_val) & (changes_aggregated_month < thr_val)])
    sum_all = np.sum(changes_aggregated_month)

    return (sum_outliers/sum_all), np.mean(changes_aggregated_month)

# makes a folium map
def make_folium_map(json_map_path, object_path,  color_func, vmin, vmax, colors_table,location, zoom_start, legend_name  ):

    cantons_path = os.path.join('', json_map_path)

    topo_json_data = json.load(open(cantons_path))
    m = folium.Map(location=location, zoom_start=zoom_start)
    folium.TopoJson(
        topo_json_data,
        object_path=object_path,
        style_function=lambda feature: {
            'fillColor': color_func(feature['id']),
            'fillOpacity': 0.9,
            'line_opacity':0.3,
            'weight': 0.4,

            }
        ).add_to(m)
    linear = folium.colormap.StepColormap( colors=colors_table, vmin=vmin, vmax=vmax,  caption=legend_name).add_to(m)

    return m;
