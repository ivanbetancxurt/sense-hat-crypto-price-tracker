from sense_hat import SenseHat
import constants
from main_menu import MainMenu
from chart import Chart

sense = SenseHat()

current_screen = 'main' # initialize screen state

main_menu = MainMenu(sense) # create main menu screen
btc_chart = Chart(sense, 'bitcoin') # create bitcoin chart screen

sense.clear() # clear any residue
while True:
    if current_screen == 'main': 
        current_screen = main_menu.display()

    # todo: display() functions for charts should also return screen state like main_menu
    elif current_screen == 'btc': 
        btc_chart.display()

    elif current_screen == 'eth': 
        sense.set_pixel(1, 5, constants.ETH_PURPLE)

    elif current_screen == 'xrp': 
        sense.set_pixel(1, 5, constants.XRP_GREEN)

    elif current_screen == 'sol': 
        sense.set_pixel(1, 5, constants.SOL_CYAN)