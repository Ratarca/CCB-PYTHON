"""
    Syntax

####> 1º Style

if condition:
    #Do something

###> 2º Style

if condition:
    #Do something
else:
    #Do another thing

###> 3º Style

if condition:
    #Do something

elif condition:
    #Do something

else:
    #Do another thing

"""

savings = 18
priceKnife = 20
priceWater = 5

# EX1
if savings >= priceKnife:
    print('I buy one car!')
    print("Now i've {}",(savings - priceKnife))

# EX2
if savings >= priceKnife:
    print('I buy one Knige!')
    print("Now i've ${}",(savings - priceKnife))
else:
    print("I can't buy a knife")

# EX3
if savings >= priceKnife:
    print('I buy aknife!')
elif savings >= priceWater:
    print('I buy water')
else:
    print('I buyed nothing : Y_Y ')