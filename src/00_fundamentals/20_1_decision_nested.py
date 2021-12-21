"""
    Syntax

####> 1º Style

if condition:
    #Do A
    if condition:
        #Do B
    else:
        #Do C
else:
    # Do B
"""

hour = 13

if 6 <= hour < 18:
    if hour > 12:
        print("Tarde")
    else:
        print("Manha")
else:
    print("Noite")