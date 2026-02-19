numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numbers = [10, 20, 30, 40]
plus_five = list(map(lambda x: x + 5, numbers))
print(plus_five)

words = ["apple", "banana", "cherry"]
upper_words = list(map(lambda word: word.upper(), words))
print(upper_words)

prices = [19.99, 5.49, 12.00]
rounded_prices = list(map(lambda price: round(price), prices))
print(rounded_prices)

names = ["emil", "tobias", "linus"]
capitalized_names = list(map(lambda name: name.capitalize(), names))
print(capitalized_names)


