"""
    Syntax
myList = [element1, ...., elementN]

    #Methods
- append : 
- extends:
- insert :
- pop    :
- sort   :

"""
cars = ['GT86', 'Impreza','Civic','Gol','Astra','Fusca']
newCars = ['Tesla','Abracada','Sopapos']

cars.append('Chevette')
cars.extend(newCars)
cars.insert(0,'ERROR')
cars.pop(0) # Remove by index default is -1
sorted(cars)
