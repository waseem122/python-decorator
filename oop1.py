class Vehicle:
    wheels = 4
    def __init__(self, name):
        self.name = name
        print(f'This {self.name} car has {Vehicle.wheels} wheels')

    
car = Vehicle('Toyota')
Vehicle.wheels = 3
print(Vehicle.wheels)
car = Vehicle('Toyota')
car2 = Vehicle('Honda')

