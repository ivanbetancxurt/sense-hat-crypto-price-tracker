from sense_hat import SenseHat
from dotenv import load_dotenv
import os

sense = SenseHat()

# get api key
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

class MainMenu():
    def __init__(self):
        # initial cursor position
        self.x= 0
        self.y = 0 
        
        self.touched = False # flag for whether user has made any input

    # display main meny
    def display(self):
        # display cursor at (0, 0) at the start of program
        if not self.touched:
            sense.set_pixels(BACKGROUND)
            sense.set_pixel(self.x, self.y, WHITE)

        inputs = sense.stick.get_events()  # get list of joystick inputs
        prev_x, prev_y = self.x, self.y # get previous cursor position

        # update cursor position
        for input in inputs:
            if input.action == 'pressed':
                self.touched = True
                if input.direction == 'up':
                    self.y = (self.y - 1) % 8
                elif input.direction == 'down':
                    self.y = (self.y + 1) % 8
                elif input.direction == 'left':
                    self.x = (self.x - 1) % 8
                elif input.direction == 'right':
                    self.x = (self.x + 1) % 8
                    
                else: # display coin name when coin is clicked
                    if (self.x, self.y) in BTC_AREA:
                        sense.show_message('Bitcoin', 0.05)
                    elif (self.x, self.y) in ETH_AREA:
                        sense.show_message('Ethereum', 0.05)
                    elif (self.x, self.y) in XRP_AREA:
                        sense.show_message('XRP', 0.05)
                    elif (self.x, self.y) in SOL_AREA:
                        sense.show_message('Solana', 0.05)

                # update screen
                sense.set_pixels(BACKGROUND)
                sense.set_pixel(prev_x, prev_y, BACKGROUND[(prev_y * 8) + prev_x])
                sense.set_pixel(self.x, self.y, WHITE)


main_menu = MainMenu()
sense.clear()

while True:
    main_menu.display()