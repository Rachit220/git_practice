# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The animal makes a sound.")


# Dog subclass
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")


# Cat subclass
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")


#  Using the classes
animal = Animal("Generic Animal")
dog = Dog("Rocky")
cat = Cat("Pokiee")

animal.speak()
dog.speak()
cat.speak()
