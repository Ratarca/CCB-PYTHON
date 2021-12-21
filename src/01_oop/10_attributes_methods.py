"""
    Syntax

---
"""
class Scout():
    bag = ['Pot','Knife','Rope']
    
    def __init__(self, name, sex, weight):
        self.name = name
        self.sex = sex
        self.weight = weight
        self.force = self._force
        self.skillSwiming = self._skillSwiming

    def speak(self, text):
        print(text)
        return text
        

    @property
    def _skillSwiming(self):
        return 1

    
    def swimming(self):
        if self.skillSwiming == True:
            print("Swimming")
        else:
            print("Drowning")

    @property
    def _force(self):
        if self.weight > 0:
            self.force = (self.weight/2)
            return self.force
        else:
            self.force = 0
            return self.force

    # https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
    @staticmethod
    def make_fire():
        print("Make fire")

    @classmethod
    def rope(cls):
        pass

ratarca = Scout("Ratarca","M",95)
ratarca.swimming()