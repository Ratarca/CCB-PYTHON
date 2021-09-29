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

savings = 18000
priceCar = 20000
priceMotorCycle = 5000

# EX1
if savings >= priceCar:
    print('I buy one car!')
    print("Now i've {}",(savings - priceCar))

# EX2
if savings >= priceCar:
    print('I buy one car!')
    print("Now i've {}",(savings - priceCar))
else:
    print("I can't buy a car")

# EX3
if savings >= priceCar:
    print('I buy a car!')
elif savings >= priceMotorCycle:
    print('I buy a motorcycle')
else:
    print('I print nothing : Y_Y ')