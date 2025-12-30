# Creating a parent class named Animal
# This class will be used to demonstrate polymorphism
class Animal:

    # Method to make a sound
    # This method will be overridden by child classes
    def sound(self):
        print("Animal makes a sound")


# Creating a child class Dog
class Dog(Animal):

    # Overriding the sound method
    def sound(self):
        print("Dog barks")


# Creating a child class Cat
class Cat(Animal):

    # Overriding the sound method
    def sound(self):
        print("Cat meows")


# Creating objects of different classes
dog = Dog()
cat = Cat()

# Calling the same method on different objects
# Each object responds in its own way
dog.sound()   # Output: Dog barks
cat.sound()   # Output: Cat meows
