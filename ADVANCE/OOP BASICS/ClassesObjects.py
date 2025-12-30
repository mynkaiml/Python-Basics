# Creating a class named Car
# A class is like a blueprint for creating objects
class Car:

    # __init__ is a constructor
    # It runs automatically when a new object of the class is created
    def __init__(self, brand, model):

        # self.brand stores the brand name of the car
        self.brand = brand

        # self.model stores the model name of the car
        self.model = model

    def prints(self):
        print("You brand name is: ",self.brand ,"\nYour model is : ", self.model)


# Creating an object (instance) of the Car class
# Here, "Toyota" is passed to brand and "Fortuner" to model
my_car = Car("Toyota", "Fortuner")

# Accessing the brand attribute of the object
print(my_car.brand)   # Output: Toyota

my_car.prints()

