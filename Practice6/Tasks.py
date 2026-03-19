import os
import shutil
from functools import reduce

#file handling

def file_handling():
    print("\n--- FILE HANDLING ---")

    filename = "sample.txt"

    with open(filename, "w") as f:
        f.write("Hello\n")
        f.write("This is sample data\n")

    with open(filename, "r") as f:
        print("\nFile content:")
        print(f.read())

    with open(filename, "a") as f:
        f.write("New line added\n")

    with open(filename, "r") as f:
        print("\nAfter append:")
        print(f.read())

    shutil.copy(filename, "backup.txt")
    print("\nBackup created: backup.txt")

    if os.path.exists("backup.txt"):
        os.remove("backup.txt")
        print("Backup file deleted safely")


#directory  exercices

def directory_handling():
    print("\n--- DIRECTORY HANDLING ---")

    os.makedirs("test_dir/sub_dir", exist_ok=True)
    print("Directories created")

    with open("test_dir/file1.txt", "w") as f:
        f.write("File 1")
    with open("test_dir/file2.py", "w") as f:
        f.write("print('Hello')")

    print("\nFiles in test_dir:")
    for item in os.listdir("test_dir"):
        print(item)

    print("\n.txt files:")
    for file in os.listdir("test_dir"):
        if file.endswith(".txt"):
            print(file)

    shutil.move("test_dir/file1.txt", "test_dir/sub_dir/file1.txt")
    print("\nMoved file1.txt into sub_dir")

    shutil.copy("test_dir/file2.py", "test_dir/sub_dir/file2_copy.py")
    print("Copied file2.py into sub_dir")


#built in functions

def built_in_functions():
    print("\n--- BUILT-IN FUNCTIONS ---")

    nums = [1, 2, 3, 4, 5]

    squares = list(map(lambda x: x**2, nums))
    print("\nSquares using map:", squares)

    evens = list(filter(lambda x: x % 2 == 0, nums))
    print("Even numbers using filter:", evens)

    total = reduce(lambda x, y: x + y, nums)
    print("Sum using reduce:", total)

    print("\nEnumerate:")
    for i, val in enumerate(nums):
        print(i, val)

    names = ["A", "B", "C"]
    scores = [90, 80, 70]

    print("\nZip:")
    for name, score in zip(names, scores):
        print(name, score)

    x = "123"

    print("\nType checking:")
    print(isinstance(x, str)) 


    num = int(x)
    print("Converted to int:", num)

    fl = float(num)
    print("Converted to float:", fl)

    st = str(fl)
    print("Converted to string:", st)


#main

def main():
    file_handling()
    directory_handling()
    built_in_functions()

if __name__ == "__main__":
    main()