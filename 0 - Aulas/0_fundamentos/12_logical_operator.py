"""
    Classic comparsion operator
    - And : &
    - OR : |
"""

myAge = 10
sisterAge = 18
brotherAge = 30

otp1 = (myAge < sisterAge) & (myAge < brotherAge) #True/True = True , because AND!
otp  = (sisterAge > myAge) | (sisterAge > brotherAge) #True/False = True, because