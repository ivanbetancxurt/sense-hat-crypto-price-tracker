import constants

class MainMenu():
    def __init__(self, sense):
        self.sense = sense # sense hat

        # initial cursor position
        self.x= 0
        self.y = 0 
        
        self.touched = False # flag for whether user has made any input

    # display main menu
    def display(self):
        # display cursor at (0, 0) at the start of program
        if not self.touched:
            self.sense.set_pixels(constants.BACKGROUND)
            self.sense.set_pixel(self.x, self.y, constants.WHITE)

        new_screen = 'main' # initialize screen state to be modified and/or returned

        inputs = self.sense.stick.get_events()  # get list of joystick inputs
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

                elif input.direction == 'middle': # display coin name, update screen state, and don't redraw main menu
                    if (self.x, self.y) in constants.BTC_AREA:
                        self.sense.show_message('Bitcoin', 0.05)
                        new_screen = 'btc'
                        break
                    elif (self.x, self.y) in constants.ETH_AREA:
                        self.sense.show_message('Ethereum', 0.05)
                        new_screen = 'eth'
                        break
                    elif (self.x, self.y) in constants.XRP_AREA:
                        self.sense.show_message('XRP', 0.05)
                        new_screen = 'xrp'
                        break
                    elif (self.x, self.y) in constants.SOL_AREA:
                        self.sense.show_message('Solana', 0.05)
                        new_screen = 'sol'
                        break

                # update screen
                self.sense.set_pixels(constants.BACKGROUND)
                self.sense.set_pixel(prev_x, prev_y, constants.BACKGROUND[(prev_y * 8) + prev_x])
                self.sense.set_pixel(self.x, self.y, constants.WHITE)

        return new_screen