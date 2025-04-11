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
        
                # update screen
                sense.set_pixels(BACKGROUND)
                sense.set_pixel(prev_x, prev_y, BACKGROUND[(prev_y * 8) + prev_x])
                sense.set_pixel(self.x, self.y, WHITE)


main_menu = MainMenu()
sense.clear()

while True:
    main_menu.display()