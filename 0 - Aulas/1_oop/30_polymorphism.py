"""
    # SUMARY
- 
-
"""

class Mammal():
    def __init__(self, name:str):
        self.name = name

    def speak(self):
        print("Speaking how mammal")


class Dog(Mammal):
    def __init__(self,name:str, years:int):
        super().__init__(name)
        self.years = years
        
    
    def speak(self):
        print("Speaking how Dog")

# Tip : Liskov principle