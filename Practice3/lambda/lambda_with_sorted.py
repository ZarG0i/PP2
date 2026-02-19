students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

numbers = [12, 5, 30, 1, 18]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)

numbers = [12, 5, 30, 1, 18]
sorted_desc = sorted(numbers, key=lambda x: x, reverse=True)
print(sorted_desc)

products = [("Phone", 999), ("Mouse", 25), ("Keyboard", 75)]
sorted_products = sorted(products, key=lambda x: x[1])
print(sorted_products)

people = [
  {"name": "Emil", "age": 25},
  {"name": "Tobias", "age": 22},
  {"name": "Linus", "age": 28}
]
sorted_people = sorted(people, key=lambda person: person["name"])
print(sorted_people)
