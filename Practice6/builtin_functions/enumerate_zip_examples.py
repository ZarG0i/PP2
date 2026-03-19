nums = [10, 20, 30]
letters = ['a', 'b', 'c']

# Example 1: enumerate
for i, val in enumerate(nums):
    print(i, val)

# Example 2: enumerate with start
for i, val in enumerate(nums, start=1):
    print(i, val)

# Example 3: zip
print(list(zip(nums, letters)))

# Example 4: zip loop
for n, l in zip(nums, letters):
    print(n, l)

# Example 5: sorted + builtins
print(sorted(nums, reverse=True))
print(len(nums), sum(nums), min(nums), max(nums))