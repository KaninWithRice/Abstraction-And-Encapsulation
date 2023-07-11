# Mohammad Mishal S. Noroña | BSCPE 1-5 | Car Class
# Create a Class
class Car:
# Create attributes Year Model, Make and Speed
    def __init__ (car, yrmodel = 2019, make = "Honda", speed = 0):
        car.__yrmodel = yrmodel
        car.__make = make
        car.__speed = speed
    def yrmodel (car):
        return car.__yrmodel
    def make (car):
        return car.__make
# Accelaration Function
    def acceleration (car):
        car.__speed += 5
# Brake Function
    def brake (car):
        car.__speed += 5
# Speed Function
    def speed (car):
        return car.__speed
    def show_speed (car):
        print("The car is speed now at : ", + car.__speed, "kmph")