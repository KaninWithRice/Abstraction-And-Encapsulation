# Mohammad Mishal S. Noroña | BSCPE 1-5 | Pet Class
# Create a Class
class Pet:
# Create a Constructor
    def __init__ (pet, name, type, age):
        pet.__name = name
        pet.__type = type
        pet.__age = age
# Name Function
    def set_name (pet, name):
        pet.__name = name
    def get_name (pet):
        return pet.__name
# Animal Type Function
    def set_type (pet, type):
        pet.__type = type
    def get_type (pet):
        return pet.__type
# Age Function
# Output