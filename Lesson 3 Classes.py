class Dog:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def bark(self):
        print (self.name + " " + self.sound)

def main():
    newDog = Dog("Pizza", 82, "blegh")
    betterDog = Dog("Calzone", 36, "woop")

    newDog.bark()
    betterDog.bark()
    
main()
