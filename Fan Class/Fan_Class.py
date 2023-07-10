# Mohammad Mishal S. Noroña | BSCPE 1-5 | Fan Class
# Create a class
class Fan:
# Add Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
    SLOW = 1
    MEDIUM = 2
    FAST = 3
# Create a Constructor
    def __init__(fan, speed = SLOW, status = False, radius = 5, color = "Blue"):
        fan.__speed = speed
        fan.__status = status
        fan.__radius = radius
        fan.__color = color
# Speed Function
    def get_speed(fan):
        return fan.__speed
    def set_speed(fan, speed):
        fan.__speed = speed
# Status Function
    def get_status(fan):
        return fan.__status
    def set_status(fan, status):
        fan.__status = status
# Radius Function
# Color Function