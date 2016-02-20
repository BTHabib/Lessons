import random

class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0
        self.distance = 0
    def __lt__(self, other):
        return self.distance < other.distance
    def setSpeed (self, speed):
        self.speed = speed
    def getSpeed (self):
        return self.speed
    def getDistance (self):
        return self.distance
    def getName (self):
        return self.name
    def move(self, time):
        self.distance += self.speed * time

def main():
    names = ["David", "Justin", "Miles"]
    cars = []
    for name in names:
        car = Car(name)
        cars.append(car)

    racing = True
    while (racing):
        for car in cars:
            car.setSpeed(random.randint(0,300))
            car.move(.25)
        for car in cars:
            if (car.getDistance() >= 10000):
                racing = False
                print ("THE WINNER IS " + car.getName())
                cars.sort()
                for x in cars:
                    print (x.getName() + " - " + str(x.getDistance()))
        
    

main()
