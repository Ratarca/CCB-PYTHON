"""
    Syntax

# basic
nameFunction = lambda x : x

# Using if and else
# Nested if

"""

# EX 1
force_round = lambda x : round(x,2)
number = 3.14159265359

print(force_round(number))

# EX 2
trafic_attorney = lambda velocity : True if velocity > 50 else False

# EX 3 
f = lambda x: 1 if x>0 else 0 if x ==0 else -1