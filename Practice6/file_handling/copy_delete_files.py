import os
os.remove("demofile.txt")

import shutil
import os
from pathlib import Path

# Example 1: copy file
shutil.copy("write.txt", "copy.txt")

# Example 2: move file
shutil.move("copy.txt", "moved_copy.txt")

# Example 3: delete file
if os.path.exists("moved_copy.txt"):
    os.remove("moved_copy.txt")

# Example 4: pathlib check
p = Path("write.txt")
print(p.exists())

# Example 5: copy entire directory
shutil.copytree("file_handling", "backup_file_handling", dirs_exist_ok=True)