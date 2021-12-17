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

savings = 50
stockPrice = 20
cdbPrice = 5

# EX1
if savings >= stockPrice:
    print('I buy one stock!')
    print(f"Now i've $ {(savings - stockPrice)}" ,'\n')

# EX2
if savings >= stockPrice:
    print('I buy one stock!')
    print(f"Now i've $ {(savings - stockPrice)}",'\n')
else:
    print("I can't buy a stock",'\n')

# EX3
if savings >= stockPrice:
    print('I buy Stock!','\n')
elif savings >= cdbPrice:
    print('I buy CDB','\n')
else:
    print('I buyed nothing : Y_Y ','\n')