"""
"""

class Flashlight():
    def __init__(self):
        pass

    def lighten(self,objectTarget:str):
        var = f"LIGHTEN : {objectTarget}"
        return var
class Scout():
    def __init__(self,name:str, flash: Flashlight):
        self.name = name
        self.flash = flash

    def speak(self, Text:str):
        print(f"{Text}")

    def light(self, target):
        return self.flash.lighten(target)

fenix = Flashlight()
ratarca = Scout("Ratarca",fenix)
print( ratarca.light('MONKEY') )

# TIP : Dependency Inversion Principle