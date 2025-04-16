import constants

class MainMenu():
    def __init__(self, sense):
        self.sense = sense # sense hat

        # initial cursor position
        self.x = 0
        self.y = 0 
        
        self.touched = False # flag for whether user has made any input

    # display main menu
    def display(self):
        # display cursor at starting position at the start of program
        if not self.touched:
            self.sense.set_pixels(constants.BACKGROUND)
            self.update_cursor(0, 0, constants.WHITE)

        new_screen = 'main' # initialize screen state to be modified and/or returned

        inputs = self.sense.stick.get_events()  # get list of joystick inputs
        prev_x, prev_y = self.x, self.y # get previous cursor position

        # update cursor position
        for input in inputs:
            if input.action == 'pressed':
                self.touched = True
                if input.direction == 'up':
                    self.y = (self.y - 4) % 8
                elif input.direction == 'down':
                    self.y = (self.y + 4) % 8
                elif input.direction == 'left':
                    self.x = (self.x - 4) % 8
                elif input.direction == 'right':
                    self.x = (self.x + 4) % 8

                elif input.direction == 'middle': # display coin name, update screen state, and don't redraw main menu
                    if (self.x, self.y) == (0, 0):
                        self.sense.show_message('Bitcoin', 0.05)
                        new_screen = 'btc'
                        break
                    elif (self.x, self.y) == (4, 0):
                        self.sense.show_message('Ethereum', 0.05)
                        new_screen = 'eth'
                        break
                    elif (self.x, self.y) == (0, 4):
                        self.sense.show_message('XRP', 0.05)
                        new_screen = 'xrp'
                        break
                    elif (self.x, self.y) == (4, 4):
                        self.sense.show_message('Solana', 0.05)
                        new_screen = 'sol'
                        break

                # update screen
                self.update_cursor(prev_x, prev_y, constants.BLACK)
                self.update_cursor(self.x, self.y, constants.WHITE)
                

        return new_screen

    def update_cursor(self, x, y, color):
        for dx in range(4):
            self.sense.set_pixel(x + dx, y, color) # draw the top and bottom of square
            self.sense.set_pixel(x + dx, y + 3, color)
            if dx == 0 or dx == 3: # draw the sides
                self.sense.set_pixel(x + dx, y + 1, color)
                self.sense.set_pixel(x + dx, y + 2, color)