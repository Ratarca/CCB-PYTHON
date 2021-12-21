"""
# Inheritance : Extends ... is a
# mro

# Composition : Has a

https://stackoverflow.com/questions/222877/what-does-super-do-in-python-difference-between-super-init-and-expl
http://python-history.blogspot.com/2010/06/inside-story-on-new-style-classes.html
https://stackoverflow.com/questions/1848474/method-resolution-order-mro-in-new-style-classes/27670178#27670178
https://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python/19950198#19950198


"""

# Human > scout > hunter/explorer || scientist || engineer
# Human > Employee

class Human():
    def __init__(self, name:str):
        self.name = name
    
    def speak(self):
        print("Hello i'm :{self.name}")

    
class economist(Human):
    def __init__(self, university:str):
        self.university = university
        super().__init__()
        


ratarca = economist(name = 'Ratarca', university='USP')
ratarca.speak()