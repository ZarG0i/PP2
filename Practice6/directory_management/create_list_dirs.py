import os

# Example 1: create directory
os.mkdir("test_dir")

# Example 2: create nested directories
os.makedirs("parent/child/grandchild", exist_ok=True)

# Example 3: list directory contents
print(os.listdir("."))

# Example 4: current working directory
print(os.getcwd())

# Example 5: change directory
os.chdir("test_dir")
print(os.getcwd())