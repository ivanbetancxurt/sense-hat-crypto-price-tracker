from sense_hat import SenseHat
import constants
from main_menu import MainMenu
from chart import Chart

sense = SenseHat()

current_screen = 'main' # initialize screen state

main_menu = MainMenu(sense) # create main menu screen
btc_chart = Chart(sense, 'bitcoin') # create bitcoin chart screen
eth_chart = Chart(sense, 'ethereum') # create ethereum chart screen
xrp_chart = Chart(sense, 'ripple') # create xrp chart screen
sol_chart = Chart(sense, 'solana') # create solana chart screen

sense.clear() # clear any residue
while True:
    if current_screen == 'main': 
        current_screen = main_menu.display()

    # todo: display() functions for charts should also return screen state like main_menu
    elif current_screen == 'btc': 
        btc_chart.display()

    elif current_screen == 'eth': 
        eth_chart.display()

    elif current_screen == 'xrp': 
        xrp_chart.display()

    elif current_screen == 'sol': 
        sol_chart.display()