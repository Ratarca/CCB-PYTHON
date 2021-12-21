"""
    Classic type variables
    - Sum : +
    - Minus : -
    - Multiple : *
    - Division : /
    - Power: **
    - Rest : %

"""

x0 = 2
x1 = 10
x2 = 20
x3 = x1 + x2
x4 = ((x3 / x1) ** 2) + x0

# Easy to show
listVar = [x0, x1,x2,x3,x4]
for val in listVar:
    print(val, '\n')
