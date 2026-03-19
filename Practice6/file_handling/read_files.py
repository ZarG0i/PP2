f = open("demofile.txt")
print(f.read())

# 5 examples of reading files

# Example 1: read()
with open("example.txt", "r") as f:
    print(f.read())

# Example 2: readline()
with open("example.txt", "r") as f:
    print(f.readline())

# Example 3: readlines()
with open("example.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# Example 4: loop through file
with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())

# Example 5: read first N characters
with open("example.txt", "r") as f:
    print(f.read(10))