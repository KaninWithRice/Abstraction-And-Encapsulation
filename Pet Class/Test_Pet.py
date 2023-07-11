# Mohammad Mishal S. Noroña | BSCPE 1-5 | Pet Class
# Import the Class
from Pet_Class import Pet
ui = Pet
# Ask user for Input
print("Good Day Fur Parents Please Enter the Following Details to Continue")
ui.get_name = input("Enter the name of your Pet : ")
ui.get_type = input("Enter The Type of Animal : ")
ui.get_age = input("Enter the age of your Pet : ")

# Show Output
ui.output()