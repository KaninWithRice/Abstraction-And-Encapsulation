# Mohammad Mishal S. Noroña | BSCPE 1-5 | Fan Class
# Import Colorama
import colorama
from colorama import Fore, Back, Style
colorama.init()
# Import Class
from Fan_Class import Fan
# Create a Loop
def start():
# Introduction
    print("")
    print(Fore.CYAN + "WELCOME TO FAN GENERATOR".center(40," ") )
    print(Fore.YELLOW + "By: Mishal Noroña".center(40," ") + Fore.WHITE )
# Create Two Fan Object
    fan1 = Fan()

    fan1.set_speed(Fan.FAST)
    fan1.set_color("Yellow")
    fan1.set_radius(10)
    fan1.set_status(True)
    
    print(Fore.LIGHTYELLOW_EX), fan1.display_fan()
start()


