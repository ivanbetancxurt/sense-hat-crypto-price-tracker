import os
from dotenv import load_dotenv

# url
URL = 'https://api.coingecko.com/api/v3/coins'

# api key
load_dotenv()
API_KEY = os.environ.get('API_KEY')

# colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BTC_YELLLOW = [252, 186, 3]
ETH_PURPLE = [165, 66, 227]
XRP_GREEN = [68, 179, 46]
SOL_CYAN = [52, 235, 189]
GREEN = [41, 199, 10]
RED = [219, 26, 36]

# coin UI
BTC_AREA = [(1, 1), (2, 1), (1, 2), (2, 2)]
ETH_AREA = [(5, 1), (6, 1), (5, 2), (6, 2)]
XRP_AREA = [(1, 5), (2, 5), (1, 6), (2, 6)]
SOL_AREA = [(5, 5), (6, 5), (5, 6), (6, 6)]