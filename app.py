from sense_hat import SenseHat
import constants
from main_menu import MainMenu

sense = SenseHat()

current_screen = 'main' # initialize screen state

main_menu = MainMenu(sense) # create main menu screen

sense.clear() # clear any residue
while True:
    if current_screen == 'main':
        current_screen = main_menu.display()
    elif current_screen == 'btc':
        sense.set_pixel(1, 5, constants.BTC_YELLLOW)
    elif current_screen == 'eth':
        sense.set_pixel(1, 5, constants.ETH_PURPLE)
    elif current_screen == 'xrp':
        sense.set_pixel(1, 5, constants.XRP_GREEN)
    elif current_screen == 'sol':
        sense.set_pixel(1, 5, constants.SOL_CYAN)