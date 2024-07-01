#inheritance
class Bus:
    def __init__(self, color, merk, speed) -> None:
        self.color = color
        self.merk = merk
        self.speed = speed

    def customBus(self) :
        self.color = "Blue"
        self.merk = "Scania"

class DobleDecker(Bus) :
    def turbo(self) :
        self.speed += 20

#normal_bus
bus_1 = Bus("White", "Mercedez", 100)
print(bus_1.color)
print(bus_1.merk)
print(bus_1.speed)

bus_DD_1 = DobleDecker("Black", "Hino", 220)
print(bus_DD_1.speed)
bus_DD_1.turbo()
print(bus_DD_1.speed)
print("\n")

#override
class Bus:
    def __init__(self, color, merk, speed):
        self.color = color
        self.merk = merk
        self.speed = speed
    
    def add_speed(self):
        self.speed += 10

class DoubleDecker(Bus):
    def turbo(self):
        self.speed += 50
    
    def add_speed(self):    
        self.speed += 20
Bus_1 = DoubleDecker("Black", "Scania", 160)
print(Bus_1.speed)
Bus_1.add_speed() 
print(Bus_1.speed)
print("\n")

#super()
class Bus:
    def __init__(self, color, merk, speed):
        self.color = color
        self.merk = merk
        self.speed = speed
    
    def add_speed(self):
        self.speed += 10

class DoubleDecker(Bus):
    def turbo(self):
        self.speed += 50
    
    def add_speed(self):    
        super().add_speed()
        print("Your speed increased, be careful")

Bus_1 = DoubleDecker("Black", "Scania", 160)
Bus_1.add_speed() 
print(Bus_1.speed)