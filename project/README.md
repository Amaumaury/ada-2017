# Title "Wikipedia Changes and World Events”

# Abstract

Looking at recent events, we noticed that entities 
Browsing some wikipedia pages, we noticed that actors involved in main events (e.g. Carles Puigdemont during the Barcelona crisis) get their english wikipedia page updated many times in a short amount of time after the event. Thus, we would like to use Wikipedia datasets, showing changes in Wikipedia pages, and combine it with events datasets, such as conflict, natural disaster or important news. We’re planning to use only english speaking wikipedia and mainly the number of changes and its timestamps, not the content itself. The goal of the project is to correlate the traffic and number of changes for the pages related to the event with the event time (from events dataset). In addition to this, we’re planning to analyse how deep in the event related pages’ network the changes are done and if these characteristics vary by time or country. By analysing different features for different types of event, we could even try to predict the events happening just by looking at the wikipedia statistics. 

# Research questions
A list of research questions you would like to address during the project. 

1. Is the number of changes in country-clustered Wikipedia information (number of pages, major edits to existing pages) a good indicator of stability of the country? 

2. How fast, how far, and for how long are the news about events (.e.g. Conflict between countries) spread in Wikipedia (for the country page and related pages)?
(this is to be analysed if we have time, its more complicate)

3. Maybe, for some events, we could observe a lot of changes in wikipedia directly before the occurrence of the event ?

4. Is it possible to predict / detect an event and its location from Wikipedia statistics?

5. Compare how deep the effect a certain event has on the Wikipedia pages network between different time eras.

# Dataset
List the dataset(s) you want to use, and some ideas on how do you expect to get, manage, process and enrich it/them. Show us you've read the docs and some examples, and you've a clear idea on what to expect. Discuss data size and format if relevant.

### Wikipedia:
1. Wikipedia API (requests)

### Event data:
1. UCDP Dataset, link: http://ucdp.uu.se/downloads/ (we proved with Ukraine data analysis that its not perfect)
2. GDELT, link : https://www.gdeltproject.org/data.html#rawdatafiles
3. Our own knowledge (Barcelona leaving Spain, UK leaving EU)

# A list of internal milestones :

1. Get cluster of wikipedia pages for a few countries.[Rescheduled]
2. Find a way to link events to some wikipedia pages.  [Done]
3. Study the impact of main events on the country-clustered wikipedia pages [ work in progress, analyse more events ]
4. Study Changes of wikipedia as an impact on stability of the country [ work in progress, analyse more countries, make a world map not only Europe]
4. Improve event detector for wikipedia changes
5. Add multiple wikipedia pages (tree) to single events
6
