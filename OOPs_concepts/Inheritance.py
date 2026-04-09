class Animal:
    def eat(self):
        print("Eating")
    def sleep(self):
        print("Sleeping")
class Dog(Animal):   
    def bark(self):
        print("Barking")
d = Dog()
d.eat()  
d.sleep()  
d.bark()  