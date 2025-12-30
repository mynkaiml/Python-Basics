# Creating a parent class named Car
# This class acts as a base class

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



# Creating a child class named ElectricCar
# This class inherits properties from the Car class

class ElectricCar(Car):

    # Constructor of the ElectricCar class
    def __init__(self, brand, model, battery_Capacity):


        # Calling the constructor of the parent class
        super().__init__(brand, model)


        # Stores battery capacity of the electric car
        self.battery_Capacity = battery_Capacity

    # Method specific to ElectricCar
    def show_Battery(self):
        print("Battery Capacity : ", self.battery_Capacity)



# Creating an object (instance) of the Car class
# Here, "Toyota" is passed to brand and "Fortuner" to model
my_car = Car("Toyota", "Fortuner")



# Creating an object of the child class
# Passing values to both parent and child class
my_electric_car = ElectricCar("Tesla", "Model 3", 75)



# Accessing the brand attribute of the object
print(my_car.brand)   # Output: Toyota

my_car.prints()



# Accessing parent class method
my_electric_car.prints()


# Accessing child class method
my_electric_car.show_Battery()


