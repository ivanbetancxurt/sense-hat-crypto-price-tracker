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

# main menu UI
BACKGROUND = [
    BLACK, BTC_YELLLOW, BTC_YELLLOW, BLACK, BLACK, ETH_PURPLE, ETH_PURPLE, BLACK,
    BTC_YELLLOW, BTC_YELLLOW, BTC_YELLLOW, BTC_YELLLOW, ETH_PURPLE, ETH_PURPLE, ETH_PURPLE, ETH_PURPLE,
    BTC_YELLLOW, BTC_YELLLOW, BTC_YELLLOW, BTC_YELLLOW, ETH_PURPLE, ETH_PURPLE, ETH_PURPLE, ETH_PURPLE,
    BLACK, BTC_YELLLOW, BTC_YELLLOW, BLACK, BLACK, ETH_PURPLE, ETH_PURPLE, BLACK,
    BLACK, XRP_GREEN, XRP_GREEN, BLACK, BLACK, SOL_CYAN, SOL_CYAN, BLACK,
    XRP_GREEN, XRP_GREEN, XRP_GREEN, XRP_GREEN, SOL_CYAN, SOL_CYAN, SOL_CYAN, SOL_CYAN,
    XRP_GREEN, XRP_GREEN, XRP_GREEN, XRP_GREEN, SOL_CYAN, SOL_CYAN, SOL_CYAN, SOL_CYAN,
    BLACK, XRP_GREEN, XRP_GREEN, BLACK, BLACK, SOL_CYAN, SOL_CYAN, BLACK
]

BTC_AREA = [
    (1, 0), (2, 0), 
    (0, 1), (1, 1), (2, 1), (3, 1),
    (0, 2), (1, 2), (2, 2), (3, 2),
    (1, 3), (2, 3),
]

ETH_AREA = [
    (5, 0), (6, 0),
    (4, 1), (5, 1), (6, 1), (7, 1),
    (4, 2), (5, 2), (6, 2), (7, 2),
    (5, 3), (6, 3)
]

XRP_AREA = [
    (1, 4), (2, 4), 
    (0, 5), (1, 5), (2, 5), (3, 5),
    (0, 6), (1, 6), (2, 6), (3, 6),
    (1, 7), (2, 7),
]

SOL_AREA = [
    (5, 4), (6, 4),
    (4, 5), (5, 5), (6, 5), (7, 5),
    (4, 6), (5, 6), (6, 6), (7, 6),
    (5, 7), (6, 7)
]