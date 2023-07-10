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
    fan1 = Fan(Fan.FAST, "Yellow", 10, True)
    fan1 = Fan(Fan.SLOW, "Blue", 5, False)
# Loading Screen