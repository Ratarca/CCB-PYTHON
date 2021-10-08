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
# High-level