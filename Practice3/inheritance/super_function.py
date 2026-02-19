class Person:
  def __init__(self, name):
    self.name = name

class Student(Person):
  def __init__(self, name, grade):
    super().__init__(name)
    self.grade = grade

student1 = Student("Emil", "A")
print(student1.name)
print(student1.grade)


class Animal:
  def __init__(self, species):
    self.species = species

class Dog(Animal):
  def __init__(self, species, sound):
    super().__init__(species)
    self.sound = sound

dog1 = Dog("Dog", "Woof")
print(dog1.species)
print(dog1.sound)


class Vehicle:
  def __init__(self, brand):
    self.brand = brand

class Car(Vehicle):
  def __init__(self, brand, year):
    super().__init__(brand)
    self.year = year

car1 = Car("Toyota", 2022)
print(car1.brand)
print(car1.year)


class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

class Manager(Employee):
  def __init__(self, name, salary, department):
    super().__init__(name, salary)
    self.department = department

manager1 = Manager("Tobias", 5000, "IT")
print(manager1.name)
print(manager1.department)


class Book:
  def __init__(self, title):
    self.title = title

class EBook(Book):
  def __init__(self, title, file_size):
    super().__init__(title)
    self.file_size = file_size

ebook1 = EBook("Python Basics", "5MB")
print(ebook1.title)
print(ebook1.file_size)
