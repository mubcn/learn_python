cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car != 'bmw':
        print(car.title())
    else:
        print(car.upper())

