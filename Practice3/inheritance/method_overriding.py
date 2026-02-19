class Animal:
    def sound(self):
        print("Animal makes a sound")

class Cat(Animal):
    def sound(self):
        print("Cat says meow")

c = Cat()
c.sound()

class Shape:
    def area(self):
        print("Area not defined")

class Circle(Shape):
    def area(self):
        print("Area = πr²")

circle = Circle()
circle.area()

class Employee:
    def salary(self):
        print("Base salary")

class Manager(Employee):
    def salary(self):
        print("Salary + Bonus")

m = Manager()
m.salary()

class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car engine started")

car = Car()
car.start()

class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    def introduce(self):
        print("I am a student")

s = Student()
s.introduce()
