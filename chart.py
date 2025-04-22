from collections import defaultdict
import requests as req
import constants
import json

class Chart():
    def __init__(self, sense, coin_id, screen):
        self.sense = sense # sense hat
        self.coin_id = coin_id # coin id for api
        self.screen = screen # screen id
        self.candles = defaultdict(list) # store for candle data
        self.price_mins = {} # minimum prices of all candles per 'day' parameter
        self.scales = {} # scaling factor (how many pixels per unit of price)
        self.days = ['1', '7', '90'] # options for 'day' api paramter, maps to 30 min, 4 hours, 4 days interval per candle
        self.day_ptr = 0 # pointer for elements in self.days

    # get candles data from api and populate fields for displaying
    def fetch_candles(self):
        headers = { # initialize request headers to access 30 calls / min
            'x_cg_demo_api_key': constants.API_KEY
        }

        params = { # initialize request parameters
            'vs_currency': 'usd',
            'days': None,
        }

        for day in self.days:
            params['days'] = day # set day parameter 
            res = req.get(f'{constants.URL}/{self.coin_id}/ohlc', params=params, headers=headers) # fetch data
            
            if res.status_code == 200: # if the api responds successfully...
                self.candles[day] = res.json()[-8:] # store the last 8 candles

                lows, highs = [], [] # initialize arrays for lowest and highest prices to find extrema
                for candle in self.candles[day]:
                    lows.append(candle[3])
                    highs.append(candle[2])

                self.price_mins[day] = min(lows)
                self.scales[day] = 7 / (max(highs) - self.price_mins[day])
            else:
                # todo: error handling
                print('oh no')
        
        with open('candles.json', 'w') as f:
           json.dump(self.candles['1'], f, indent=4)

    # display chart
    def display(self):
        new_screen = self.screen # set new screen

        if not self.candles: #! for now, do not re-compute candles
            self.fetch_candles()

        for i, candle in enumerate(self.candles[self.days[self.day_ptr]]):
            _, open, high, low, close = candle
            color = constants.GREEN if open <= close else constants.RED # choose candle color based on price movement

            # map the high and low points of the candle to pixel (value from 0 to 7)
            mapped_high = 7 - int((high - self.price_mins[self.days[self.day_ptr]]) * self.scales[self.days[self.day_ptr]])
            mapped_low = 7 - int((low - self.price_mins[self.days[self.day_ptr]]) * self.scales[self.days[self.day_ptr]])

            for row in range(min(mapped_high, mapped_low), max(mapped_high, mapped_low) + 1):
                self.sense.set_pixel(i, row, color)

        for input in self.sense.stick.get_events():
            print('back to main menu')
            if input.direction == 'middle':
                if input.action == 'held': # if user holds joystick down...
                    new_screen = 'main' # ...go back to the main menu
                elif input.action == 'pressed': # if user presses joystick...
                    self.day_ptr = (self.day_ptr + 1) % len(self.days) # ...rotate 'day' parameter, showing new set of candles
            self.sense.clear()
        
        return new_screen