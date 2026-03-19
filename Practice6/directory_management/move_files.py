import shutil
import os

# Example 1: move file to folder
shutil.move("write.txt", "test_dir/write.txt")

# Example 2: rename file
os.rename("test_dir/write.txt", "test_dir/renamed.txt")

# Example 3: remove empty directory
os.rmdir("test_dir")

# Example 4: move back file
shutil.move("test_dir/renamed.txt", "renamed.txt")

# Example 5: safe delete directory
import shutil
shutil.rmtree("parent", ignore_errors=True)