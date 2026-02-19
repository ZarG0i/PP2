x = lambda a: a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

x = lambda a: a - 4
print(x(20))

x = lambda text: text.upper()
print(x("hello"))

x = lambda a, b, c: a + b + c
print(x(2, 4, 6))

check_even = lambda n: n % 2 == 0
print(check_even(8))

def power_func(n):
  return lambda a: a ** n

square = power_func(2)
cube = power_func(3)

print(square(5))
print(cube(2))
