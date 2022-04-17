"""
This is intended to be a learning of abstract classes

Essentially, you define abstract methods in an abstract class to ensure that 
it's child classes have a compulsion of having those methods defined inside them
"""

from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty


class Vehicle(ABC):
    
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def startVehicle(self):
        pass

class Car(Vehicle):
    def __init__(self, **kwargs):
        super(Car, self).__init__()
        self.model = kwargs.get('model', None)
        self.manufacturer = kwargs.get('manufacturer', None)

    def startVehicle(self):
        print("Place key in ignition")
        print("Turn key, and wait for engine to start")
        print("SUCCESS, vehicle has started")

class Plane(Vehicle):
    def __init__(self, **kwargs):
        super(Plane, self).__init__()
        self.model = kwargs.get('model', None)
        self.manufacturer = kwargs.get('manufacturer', None)

    def startVehicle(self):
        print("Captain performing pre-flight checks")
        print("Captain starting engines")
        print("Captain verifying proper startup")
        print(f"SUCCESS, {self.model} plane has started")

if __name__ == "__main__":
    plane = Plane(model="B2", manufacturer="Northrop")
    plane.startVehicle()
    print(plane.model, plane.manufacturer)



