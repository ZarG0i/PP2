with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())


with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())


f = open("myfile.txt", "x")

# 5 examples of writing/appending

# Example 1: write (overwrite)
with open("write.txt", "w") as f:
    f.write("Hello World\n")

# Example 2: append
with open("write.txt", "a") as f:
    f.write("Appended line\n")

# Example 3: write multiple lines
lines = ["Line1\n", "Line2\n"]
with open("write.txt", "w") as f:
    f.writelines(lines)

# Example 4: create file (x mode)
try:
    with open("newfile.txt", "x") as f:
        f.write("Created file")
except FileExistsError:
    print("File already exists")

# Example 5: write numbers
with open("numbers.txt", "w") as f:
    for i in range(5):
        f.write(str(i) + "\n")