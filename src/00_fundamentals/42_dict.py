"""
    Syntax
myDict = {"key0":value0, ...., "keyN":valueN}

    # Index
    myDict["keyN"]

    #Methods
- items() : Check dict with idx anda val
- keys()  : Show all keys (list)
- values(): Show all values (list)
- update(): Add new item on dict
- pop()   : Remove item by key value

# Extends operators : 
{*dict1, ... , *dictN}
dict1 | ... | dictN
"""
cars = {'GT86':100, 'Impreza':200,
        'Civic':300,'Gol':400,
        'Astra':500,'Fusca':600}

motorCycle = {'Suzuki':20}

print(cars["Astra"])
cars["Uno"] = 50

print(cars.items())
for key,val in cars.items():
    print(key, val)

cars.update({"GT86":1000})
cars.update({"Tesla":100})
cars.pop("Gol")

vehicles = cars | motorCycle #We can use too : c = {**a, **b} 