#base class
class Vehicle:
    def move(self):
        print ("vehicle is moving")

#derived class 1
class Car(Vehicle):
    def move(self):
        print("Driving on the road")

#derived class 2
class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

#Demonstrating Polymorphism                
vehicles = [Vehicle(), Car(), Bicycle()]

for v in vehicles:

    v.move()
