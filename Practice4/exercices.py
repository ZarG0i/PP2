"Date.md"
#1
from datetime import datetime, timedelta

today = datetime.now()
five_days_ago = today - timedelta(days=5)

print("Today:", today)
print("Five days ago:", five_days_ago)
#2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
#3
from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print("Original datetime:", now)
print("Without microseconds:", no_microseconds)
#4
from datetime import datetime

date1 = datetime(2026, 2, 25, 12, 0, 0)
date2 = datetime(2026, 2, 26, 14, 30, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)

#Generators
#1
def square_generator(N):
    for i in range(N+1):
        yield i ** 2


for sq in square_generator(5):
    print(sq, end=' ')
#2
def even_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i


n = int(input("Enter a number n: "))
even_numbers = list(even_generator(n))
print(",".join(map(str, even_numbers)))
#3
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


for num in divisible_by_3_and_4(50):
    print(num, end=' ')
#4
def squares(a, b):
    for i in range(a, b+1):
        yield i ** 2


for sq in squares(3, 7):
    print(sq)
#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i


for num in countdown(5):
    print(num, end=' ')

#math.md
#1
import math
degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)

print("Output radian:", radian)
#2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) * height / 2
print("Expected Output:", area)
#3
n_sides = int(input("Input number of sides: "))
side_length = float(input("Input the length of a side: "))

area = side_length ** 2 if n_sides == 4 else (n_sides * side_length ** 2) / (4 * math.tan(math.pi / n_sides))

print("The area of the polygon is:", area)
#4

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print("Expected Output:", area)