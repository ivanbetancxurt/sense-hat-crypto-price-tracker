from sense_hat import SenseHat
from main_menu import MainMenu
from chart import Chart

sense = SenseHat()

current_screen = 'main' # initialize screen state

main_menu = MainMenu(sense) # create main menu screen
btc_chart = Chart(sense, 'bitcoin', 'btc') # create bitcoin chart screen
eth_chart = Chart(sense, 'ethereum', 'eth') # create ethereum chart screen
xrp_chart = Chart(sense, 'ripple', 'xrp') # create xrp chart screen
sol_chart = Chart(sense, 'solana', 'sol') # create solana chart screen

sense.clear() # clear any residue
while True:
    if current_screen == 'main': 
        current_screen = main_menu.display()

    elif current_screen == 'btc': 
        current_screen = btc_chart.display()

    elif current_screen == 'eth': 
        current_screen = eth_chart.display()

    elif current_screen == 'xrp': 
        current_screen = xrp_chart.display()

    elif current_screen == 'sol': 
        current_screen = sol_chart.display()