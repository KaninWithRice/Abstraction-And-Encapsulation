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
        fan.__status = bool(status)
# Radius Function
    def get_radius(fan):
        return fan.__radius
    def set_radius(fan, radius):
        fan.__radius = float(radius)
# Color Function
    def get_color(fan):
        return fan.__color
    def set_color(fan, color):
        fan.__color = str(color)
# Display Function
    def display_fan(fan):
        print("Fan Details")
        print("Speed : ", fan.__speed)
        print("Status : ", fan.__status)
        print("Radius : ", fan.__radius)
        print("Color : ", fan.__color)