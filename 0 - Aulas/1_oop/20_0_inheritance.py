"""
# Inheritance : Extends ... is a
# Composition : Has a
"""

# Human > scout > hunter/explorer || scientist || engineer
# Human > Employee

class Scout():
    def __init__(self, name):
        self.name = name

    def NOTHING(self):
        return 1

    

class Hunter(Scout):
    def __init__(self,name, att2):
        super().__init__(name)
        self.att2 = att2

dx = Hunter(1,2)
print(dx.name, dx.att2)
print(dx.NOTHING())