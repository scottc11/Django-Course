age = 27

name = "Scott"

todayIsCold = True

def hello(name, age):
    print("Hello", name, "you are", age, "years old")

dogNames = ["fido", "Sean", "Sally", "Mark"]

for dog in dogNames:
    print(dog)

dogs = {"Fido": 8, "Sally": 17, "Sean": 2}

print(dogs)

class Dog:

    def __init__(self, _name, _age, _furColor):
        self.name = _name
        self.age = _age
        self.furColor = _furColor

    def bark(self, str=""):
        print("Woof!", str)

myDog = Dog("Fido", 4, "Brown")

myDog.bark()

print(myDog.age)
print(myDog.name)
