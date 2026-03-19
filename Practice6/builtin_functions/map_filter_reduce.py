from functools import reduce

nums = [1, 2, 3, 4, 5]

# Example 1: map (square)
print(list(map(lambda x: x**2, nums)))

# Example 2: map (to string)
print(list(map(str, nums)))

# Example 3: filter (even numbers)
print(list(filter(lambda x: x % 2 == 0, nums)))

# Example 4: filter (greater than 2)
print(list(filter(lambda x: x > 2, nums)))

# Example 5: reduce (sum)
print(reduce(lambda x, y: x + y, nums))