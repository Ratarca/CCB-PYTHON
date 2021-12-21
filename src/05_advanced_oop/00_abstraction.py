from abc import ABCMeta, abstractmethod
from typing import Any

class IEarthAnimal(metaclass = ABCMeta):

    @abstractmethod
    def speak(self):
        """
            Comments
        """
        pass

    @abstractmethod
    def walk(self):
        """
            Comments
        """
        pass

# implements
def Wolf(IEarthAnimal):
    def __init__(self,name:str):
        self.name = name

    def speak(self):
        print("AU AU")
    
    def walk(self):
        print("WALKING")
