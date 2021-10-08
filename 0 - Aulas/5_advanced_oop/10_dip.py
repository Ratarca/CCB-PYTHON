"""
Dependency Inversion Principle
> Abstraction class
> Low-level implementation
> High-level
"""
# Abstraction
from abc import ABCMeta, abstractmethod

class ICool(metaclass=ABCMeta):
    pass
    
    @abstractmethod
    def nothing():
        """
        """
        pass

# Low-level
class LowOne(ICool):
    pass

    def nothing():
        pass

class Lowtwo(ICool):
    pass

    def nothing():
        pass

# High-level
class HighOne():
    def __init__(self, objectCool):
        self.objectCool = objectCool
    
    def calculate():
        return self.objectCool.nothing()
