class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

class Car:
  def __init__(self, brand, speed):
    self.brand = brand
    self.speed = speed

  def accelerate(self, value):
    self.speed += value
    print(self.brand, "speed:", self.speed)

car1 = Car("Toyota", 60)
car1.accelerate(20)

class BankAccount:
  def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print("New balance:", self.balance)

account1 = BankAccount("Emil", 100)
account1.deposit(50)

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    return self.width * self.height

rect1 = Rectangle(5, 3)
print(rect1.area())

class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade

  def show_grade(self):
    print(self.name, "grade:", self.grade)

student1 = Student("Tobias", "A")
student1.show_grade()

class Light:
  def __init__(self):
    self.is_on = False

  def toggle(self):
    self.is_on = not self.is_on
    print("Light on:", self.is_on)

light1 = Light()
light1.toggle()
light1.toggle()

class Counter:
  def __init__(self):
    self.value = 0

  def increment(self):
    self.value += 1
    print("Counter:", self.value)

counter1 = Counter()
counter1.increment()
counter1.increment()

class Book:
  def __init__(self, title, pages):
    self.title = title
    self.pages = pages

  def summary(self):
    print(self.title, "-", self.pages, "pages")

book1 = Book("Python Basics", 200)
book1.summary()

class Timer:
  def __init__(self, seconds):
    self.seconds = seconds

  def add_time(self, seconds):
    self.seconds += seconds
    print("Total seconds:", self.seconds)

timer1 = Timer(30)
timer1.add_time(15)
