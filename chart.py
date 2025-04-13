from collections import defaultdict
import requests as req
import constants

class Chart():
    def __init__(self, coin_id):
        self.coin_id = coin_id 
        self.candles = defaultdict(list) # store for candle data

    # get candles data from api
    def fetch_candles(self):
        days = ['1', '7', '90'] # options for 'day' paramters, maps to 30 min, 4 hours, 4 days interval per candle

        headers = { # initialize request headers to access 30 calls / min
            'x_cg_demo_api_key': constants.API_KEY
        }

        params = { # initialize request parameters
            'vs_currency': 'usd',
            'days': None,
        }

        for day in days:
            params['days'] = day # set day parameter 
            res = req.get(f'{constants.URL}/{self.coin_id}/ohlc', params=params) # fetch data
            print(f'DAYS {day}: {res.json()}')

    def display(self):
        pass

chart = Chart('bitcoin')
chart.fetch_candles()