def add_numbers(x, y):
  return x + y

result = add_numbers(5, 3)
print(result)

def multiply_numbers(x, y):
  return x * y

result = multiply_numbers(4, 6)
print(result)


def get_fruits():
  return ["apple", "banana", "cherry"]

fruits = get_fruits()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def get_colors():
  return ["red", "blue", "green"]

colors = get_colors()
print(colors[0])
print(colors[1])
print(colors[2])


def get_coordinates():
  return (10, 20)

x, y = get_coordinates()
print("x:", x)
print("y:", y)

def get_size():
  return (1920, 1080)

width, height = get_size()
print("width:", width)
print("height:", height)


def greet_person(name, /):
  print("Hello", name)

greet_person("Emil")

def show_city(city, /):
  print("City:", city)

show_city("London")


def calculate_total(a, b, /, *, c, d):
  return a + b + c + d

result = calculate_total(5, 10, c = 15, d = 20)
print(result)

def calculate_score(base, bonus, /, *, extra, final):
  return base + bonus + extra + final

result = calculate_score(1, 2, extra = 3, final = 4)
print(result)
