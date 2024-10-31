from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    def describe(self):
        print("This is an animal that belongs to the Animal Kingdom.")

class Dog(Animal):
    def make_sound(self):
        return "Woof Woof!"
    
    def describe(self):
        super().describe()
        print("Dogs are loyal and friendly animals often kept as pets.")

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
    def describe(self):
        super().describe()
        print("Cats are independent animals that are popular as pets.")

class Cow(Animal):
    def make_sound(self):
        return "Moo!"
    
    def describe(self):
        super().describe()
        print("Cows are domesticated animals commonly found on farms.")

dog = Dog()
cat = Cat()
cow = Cow()

for animal in (dog, cat, cow):
    print(f"{animal.__class__.__name__} makes sound: {animal.make_sound()}")
    animal.describe()
    print()
