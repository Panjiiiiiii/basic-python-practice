#class
class Car : #class
    color = "Red" #attribut
mobil_1 = Car() #object
mobil_1.color = "Blue"
mobil_2 = Car()
mobil_2.color = "Orange"
print(mobil_1.color)
print(mobil_2.color)

#class constructor 1
class Moto :
    def __init__(self) -> None:
        self.color = "white"
moto_1 = Moto()
moto_2 = Moto()
print("\n")
print(moto_1.color)
print(moto_2.color)

moto_1.color = "black"
print(moto_1.color)
print(moto_2.color)

#class constructor 2
class Moto :
    def __init__(self, color, speed, merk) -> None:
        self.color = color
        self.speed = speed
        self.merk = merk
moto_1 = Moto('Merah', 200, 'GT3')
print("\n")
print(moto_1.color)
print(moto_1.speed)
print(moto_1.merk)
print("\n")

#method (decorator concept)
def my_say(func):
    def wrapper() :
        print("Before")
        func()
        print("After")
    return wrapper

@my_say
def say_hello() :
    print("Hello world")
say_hello()

#object method
class Bus:
    def __init__(self, color, merk, speed) -> None:
        self.color = color
        self.merk = merk
        self.speed = speed

    def customBus(self) :
        self.color = "Blue"
        self.merk = "Scania"
        self.speed += 100

bus_1 = Bus("Red", "Mercedez", 10)
print("\n")
print("Before modif")
print(bus_1.color)
print(bus_1.merk)
print(bus_1.speed)

bus_1.customBus()
print("After modif")
print(bus_1.color)
print(bus_1.merk)
print(bus_1.speed)
print("\n")

#static method
class laptop :
    def __init__(self, merk, ram, memory) -> None:
        self.merk = merk
        self.ram = ram
        self.memory = memory
    @staticmethod
    def open_laptop () :
        print("Hello user")
laptop.open_laptop()
laptop_1 = laptop("Lenovo", 16, 1000)
laptop_1.open_laptop()
print("\n")

#class method
class book :
    def __init__(self, page) -> None:
        self.page = page
    @classmethod
    def open_page(*cls) :
        print(cls)
book.open_page()
book_1 = book(200)
book.open_page()