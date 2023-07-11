# Mohammad Mishal S. Noroña | BSCPE 1-5 | Pet Class
# Create a Class
class Pet:
# Create a Constructor
    def __init__ (pet):
        pet.__name = ""
        pet.__type = ""
        pet.__age = ""
# Name Function
    def set_name (pet):
        pet.__name = input("Enter the name of your Pet : ")
    def get_name (pet):
        return pet.__name
# Animal Type Function
    def set_type (pet):
        pet.__type = input("Enter The Type of Animal : ")
    def get_type (pet):
        return pet.__type
# Age Function
    def set_age (pet):
        pet.__age = int(input("Enter the age of your Pet : "))
    def get_age (pet):
        return pet.__age
# Output
    def output (pet):
        print("\n<<<<---Pet Details--->>>>")
        print("Name : ", pet.__name)
        print("Type : ", pet.__type)
        print("Age  : ", pet.__age)
