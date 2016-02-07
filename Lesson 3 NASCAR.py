#Create class Car
class Car:
    #define initialization and paramaeters
    def __init__(self, name):
        #define data members
        self.name = name
        self.speed = 0
        self.distance = 0
    #start new function to define cars movement
    def move(self, time):
        self.distance += self.speed * time
#create new main function
def main():
    firstCar = Car("Justin")
    print( str(firstCar.distance))
    firstCar.speed = 60
    firstCar.move(1.5)
    print( str(firstCar.distance))

main()
