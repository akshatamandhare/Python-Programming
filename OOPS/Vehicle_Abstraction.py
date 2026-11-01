## Now let us create a new class and make it as abstract

from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, capacity):
        self.capacity = capacity

    @abstractmethod
    def start(self):
        pass

    def Display(self):            ## concrete method: The method in the abstract class which is not with abstract method
        print('You are using vehicle class')

# V = Vehicle(12)
# print(V.capacity)
# V.start()

## When we want to make any class as abstract class inherit it with ABC class present in abc module
## To make any class as abstract class we must have at least one abstract method in it
## It will restrict the user not to create the object for abstract class

