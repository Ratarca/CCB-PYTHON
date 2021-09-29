"""
    Syntax

for val in iterator:
    #Do something
"""

names = ['Rafael','Isac','Elisabeth', 'Gabis']

for v in names:
    print(f'Welcome {v}')


for idx,val in enumerate(names):
    print(idx, val)


for idx,val in enumerate(names):
    for idx2,val2 in enumerate(names):
        print(idx, idx2)