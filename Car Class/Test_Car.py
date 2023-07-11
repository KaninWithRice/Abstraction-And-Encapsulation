# Mohammad Mishal S. Noroña | BSCPE 1-5 | Car Class
# Import Class
from Car_Class import Car
# Create an Object
Car1 = Car(2019, "Honda", 0)
# Car Acceleration
print("Accelearting.....")
for acc in range(5):
    Car1.acceleration()
    Car1.show_speed()
# Car Brake
print("Braking.....")
for acc in range(5):
    Car1.brake()
    Car1.show_speed()