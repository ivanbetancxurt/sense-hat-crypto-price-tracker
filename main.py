from sense_hat import SenseHat
from dotenv import load_dotenv
import constants
import os

sense = SenseHat()

# get api key
load_dotenv()
API_KEY = os.environ.get('API_KEY')

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
            sense.set_pixels(constants.BACKGROUND)
            sense.set_pixel(self.x, self.y, constants.WHITE)

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
                    if (self.x, self.y) in constants.BTC_AREA:
                        sense.show_message('Bitcoin', 0.05)
                    elif (self.x, self.y) in constants.ETH_AREA:
                        sense.show_message('Ethereum', 0.05)
                    elif (self.x, self.y) in constants.XRP_AREA:
                        sense.show_message('XRP', 0.05)
                    elif (self.x, self.y) in constants.SOL_AREA:
                        sense.show_message('Solana', 0.05)

                # update screen
                sense.set_pixels(constants.BACKGROUND)
                sense.set_pixel(prev_x, prev_y, constants.BACKGROUND[(prev_y * 8) + prev_x])
                sense.set_pixel(self.x, self.y, constants.WHITE)


main_menu = MainMenu()
sense.clear()

while True:
    main_menu.display()