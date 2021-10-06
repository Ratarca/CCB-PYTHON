from abc import ABC, abstractmethod

class CLASS_ONE(metaclass = ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def OPTION_PRICE(self):
        pass

# implements
