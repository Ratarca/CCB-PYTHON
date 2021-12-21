"""
    Syntax
myList = [element1, ...., elementN]

    #Methods
- append : Add item (-1 index)
- extends: Extend list
- insert : Inser item on position
- pop    : Remove item by index : default is -1
- sort   : Order

"""
cars = ['GT86', 'Impreza','Civic','Gol','Astra','Fusca']
newCars = ['Tesla','Abracada','Sopapos']

cars.append('Chevette')
cars.extend(newCars)
cars.insert(0,'ERROR')
cars.pop(0) # Remove by index default is -1
sorted(cars)
