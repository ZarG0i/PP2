class Animal:
  def speak(self):
    print("Animal makes a sound")

class Dog(Animal):
  pass

dog1 = Dog()
dog1.speak()


class Vehicle:
  def move(self):
    print("Vehicle is moving")

class Car(Vehicle):
  pass

car1 = Car()
car1.move()


class Person:
  def introduce(self):
    print("Hello, I am a person")

class Student(Person):
  pass

student1 = Student()
student1.introduce()


class Shape:
  def area(self):
    print("Area method in parent class")

class Rectangle(Shape):
  pass

rect1 = Rectangle()
rect1.area()


class Employee:
  def work(self):
    print("Employee is working")

class Manager(Employee):
  pass

manager1 = Manager()
manager1.work()


class Phone:
  def call(self):
    print("Calling from phone")

class SmartPhone(Phone):
  pass

phone1 = SmartPhone()
phone1.call()
