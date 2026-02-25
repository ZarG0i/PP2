#Iterators: iter() and next()
numbers = [1, 2, 3]
it = iter(numbers)

print(next(it))  # 1
print(next(it))  # 2

#-------------------------------------

text = "ABC"
it = iter(text)

print(next(it))  # A
print(next(it))  # B
#-------------------------------------
tuple_data = (10, 20, 30)
it = iter(tuple_data)

print(next(it))
print(next(it))
print(next(it))
#Loop Through an Iterator
numbers = [10, 20, 30]
it = iter(numbers)

for num in it:
    print(num)
#-------------------------------------
word = "Python"
it = iter(word)

for letter in it:
    print(letter)
#-------------------------------------
numbers = [1, 2, 3]
for num in iter(numbers):
    print(num)

#Create an iterator 
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#-------------------------------------
class EvenNumbers:
    def __init__(self, max):
        self.current = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current <= self.max:
            return self.current
        else:
            raise StopIteration

for num in EvenNumbers(10):
    print(num)
#-------------------------------------
class Squares:
    def __init__(self, max):
        self.current = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

for num in Squares(4):
    print(num)

#Generators yield keyword
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)
#-------------------------------------
def simple_gen():
    yield 1
    yield 2
    yield 3

for value in simple_gen():
    print(value)
#-------------------------------------
def squares(n):
    for i in range(n):
        yield i * i

for num in squares(5):
    print(num)
#-------------------------------------
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)
#-------------------------------------
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(6):
    print(num)
#Creating Generator Functions
def number_generator():
    yield 1
    yield 2
    yield 3

for num in number_generator():
    print(num)
#-------------------------------------
def my_range(start, end):
    while start < end:
        yield start
        start += 1

for num in my_range(1, 5):
    print(num)
#-------------------------------------
def even_numbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)
#-------------------------------------
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(7):
    print(num)
#-------------------------------------
def word_generator(text):
    words = text.split()
    for word in words:
        yield word

for word in word_generator("Generator"):
    print(word)
#Generator expressions
gen = (x for x in range(5))
for num in gen:
    print(num)
#-------------------------------------
squares = (x*x for x in range(5))
print(list(squares))
#-------------------------------------
evens = (x for x in range(10) if x % 2 == 0)
print(list(evens))
#-------------------------------------
words = ["python", "java", "c++"]
upper_words = (word.upper() for word in words)
print(list(upper_words))
#-------------------------------------


