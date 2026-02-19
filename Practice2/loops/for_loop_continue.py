numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        continue
    print(num)

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

letters = ["a", "b", "c", "d"]
for letter in letters:
    if letter in ["b", "d"]:
        continue
    print(letter)

ages = [12, 15, 18, 20]
for age in ages:
    if age < 18:
        continue
    print(age)

numbers = [10, 20, 30, 40, 50]
for num in numbers:
    if num % 20 == 0:
        continue
    print(num)
