
## It is the process of hiding the implementation and just display the functionality to the user
## To make any class as abstract class we must use the module called as abc

# class Bike:
#     def start(self):
#         print('Starts with kick')
#
# class Car:
#     def start(self):
#         print('starts with key')
#
# class Scooty:
#     def start(self):
#         print('self start')

############################################################################################

from Vehicle_Abstraction import Vehicle

class Bike(Vehicle):
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print('Starts with kick')

class Scooty(Vehicle):
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print('Self Start')


class Car(Vehicle):
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print('Starts with key')


## When we inherit any child class with the abstract class we must have all the abstract method
## in it if not will not allow the user to create the object for the class

