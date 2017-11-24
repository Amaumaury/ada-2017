import requests

WIKI_URL = 'https://en.wikipedia.org/w/api.php'

class HistoryScraper:

    def __init__(self, wikipage_title):
        self.wikipage_title = wikipage_title
        self.payload = {'action': 'query',
                        'prop': 'revisions',
                        'titles': wikipage_title,
                        'rvprop': 'ids|flags|timestamp|comment|user|size',
                        'format': 'json',
                        'rvlimit': 500}

    def get_history(self, start_date, end_date):
        req_payload = dict(self.payload)

        # Start and end dates are inverted here as I find wikipedia ways of
        # thinking about edits history not intuitive
        req_payload['rvstart'] = end_date
        req_payload['rvend'] = start_date

        response = {'continue': True}
        revisions = []

        while 'continue' in response:
            response = requests.get(WIKI_URL, params=req_payload).json()
            response_data = list(response['query']['pages'].values())[0]['revisions']
            revisions.extend(response_data)

            if 'continue' in response:
                req_payload['rvcontinue'] = response['continue']['rvcontinue']

        return revisions
