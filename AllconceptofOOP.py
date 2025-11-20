class Bird:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def sound(self):
        print(f"{self.name} chirps happily!")
    
    def info(self):
        print(f"{self.name} is a {self.color} bird")

bird1 = Bird("Tweety", "yellow")
bird2 = Bird("Sky", "blue")

bird1.sound()
bird1.info()

bird2.sound()
bird2.info()

print()

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a generic animal sound")

class Parrot(Animal):
    def speak(self):
        print(f"{self.name} says 'Hello!'")

parrot = Parrot("Polly")
parrot.speak()
