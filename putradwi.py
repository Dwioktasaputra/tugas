from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def habitat(self):
        pass

# Subclass 1: Dog
class Dog(Animal):
    def sound(self):
        return "Bark"

    def habitat(self):
        return "Domestic"

# Subclass 2: Bird
class Bird(Animal):
    def sound(self):
        return "Chirp"

    def habitat(self):
        return "Forest or domestic"

# Subclass 3: Frog
class Frog(Animal):
    def sound(self):
        return "Croak"

    def habitat(self):
        return "Swamp"

# Program utama
def main():
    animals = [Dog(), Bird(), Frog()]

    for animal in animals:
        print(f"{animal.__class__.__name__}:")
        print(f"  Sound: {animal.sound()}")
        print(f"  Habitat: {animal.habitat()}")
        print("-" * 30)

if __name__ == "__main__":
    main()
