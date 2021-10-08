"""
    Generator & Yield
    - Theory lazy iterators / Optimize memory
    - Yield
    - Apply { Functions / batch files }
"""

commonList = [1,2,3,4,5,6,7,8,9,10]
genList = (1,2,3,4,5,6,7)
genList2 = (i for i in commonList) #Build generator

# Understand Yield

## Apply

# Function
def infinity():
    num = 0
    while True:
        
        yield num
        num += 1

infinityObject = infinity()

print(genList)
print(infinityObject)

## Batch files