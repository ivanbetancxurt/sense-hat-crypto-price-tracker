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

class Cursor():
    def __init__(self):
        # initial cursor position
        self.x= 0
        self.y = 0 
        
        self.touched = False # flag for whether user has made any input

    # track and display cursor depending on user input
    def track_cursor(self):
        inputs = sense.stick.get_events()  # get list of joystick inputs
        
        prev_x, prev_y = self.x, self.y # get previous cursor position

        # display cursor at (0, 0) at the start of program
        if not self.touched:
            sense.set_pixel(self.x, self.y, WHITE)

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
                sense.set_pixel(prev_x, prev_y, BLACK)
                sense.set_pixel(self.x, self.y, WHITE)
                

cursor = Cursor()
sense.clear()
while True:
    cursor.track_cursor()