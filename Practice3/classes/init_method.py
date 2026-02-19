class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)

class Car:
  def __init__(self, brand, year):
    self.brand = brand
    self.year = year

car1 = Car("Toyota", 2022)

print(car1.brand)
print(car1.year)

class Book:
  def __init__(self, title, pages):
    self.title = title
    self.pages = pages

book1 = Book("Python Basics", 180)

print(book1.title)
print(book1.pages)

class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

student1 = Student("Tobias", "A")

print(student1.name)
print(student1.grade)

class Animal:
  def __init__(self, species, sound):
    self.species = species
    self.sound = sound

animal1 = Animal("Dog", "Woof")

print(animal1.species)
print(animal1.sound)
