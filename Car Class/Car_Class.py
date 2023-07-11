# Mohammad Mishal S. Noroña | BSCPE 1-5 | Car Class
# Create a Class
class Car:
# Create attributes Year Model, Make and Speed
    def __init__ (car, yrmodel, make, speed):
        car.__yrmodel = yrmodel
        car.__make = make
        car.__speed = 0
# Accelaration Function
    def acceleration (car):
        car.__speed += 5
# Brake Function
    def brake (car):
        car.__speed += 5
# Speed Function
    def speed (car):
        return car.__speed