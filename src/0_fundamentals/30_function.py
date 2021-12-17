"""
    Syntax

def nameFunction(*params):
    #Code

#Scope

"""

# Syntax
def sum_vals(valA: int, valB:int) -> int:
    return valA + valB

def show_msg(msg:str, repet:int = 1) -> None:
    """
    This function sum two elements.
    """
    for idx in range(repet):
        print(f"{msg} {idx}")

# Scope
name = "RATARCA"
otherName = "KRATOS"

def show_name(name:str):
    otherName = "CLEITON"
    return [name, otherName]

show_msg("Pyhon",2)
print( show_name("SCOPE ") )