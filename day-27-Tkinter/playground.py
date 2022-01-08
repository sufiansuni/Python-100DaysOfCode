# args is a tuple, simillar to array, position matters
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,1))
print(add(1,1,1))

# kwargs is a dictionary
def calc(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calc(1, add=1, multiply=2))

class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-R")
my_car2 = Car(make="Nissan")

print(my_car.model)
print(my_car2.model)
