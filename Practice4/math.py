#Built-in Math Functions
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)
#-------------------------------------
x = abs(-7.25)

print(x)
#-------------------------------------
print(pow(2, 3))     # 8
print(pow(5, 2))     # 25
#-------------------------------------
print(round(3.14159, 2))  # 3.14
print(round(7.5))         # 8
#math Module Functions 
import math

x = math.sqrt(64)

print(x)
#-------------------------------------
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) 
print(y) 
#-------------------------------------
import math
print(math.sqrt(16)) 
#-------------------------------------
import math
print(math.sin(math.pi / 2))  
print(math.cos(0))           
#random Module
import random
print(random.random())  
#-------------------------------------
import random
print(random.randint(1, 10)) 
#-------------------------------------
import random
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))
#-------------------------------------
import random
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
#-------------------------------------
import random
dice = random.randint(1, 6)
print("Dice rolled:", dice)

