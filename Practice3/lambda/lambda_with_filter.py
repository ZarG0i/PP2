numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

numbers = [10, 25, 30, 45, 50]
greater_than_30 = list(filter(lambda x: x > 30, numbers))
print(greater_than_30)

words = ["apple", "kiwi", "banana", "fig", "cherry"]
long_words = list(filter(lambda word: len(word) > 4, words))
print(long_words)

names = ["Emil", "", "Tobias", "", "Linus"]
valid_names = list(filter(lambda name: name != "", names))
print(valid_names)
