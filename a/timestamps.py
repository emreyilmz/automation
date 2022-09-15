import os
import sys

walk_dir = "./"

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    try:
        print( root)
        hello = root+'/timestamps.vtt'
        print(hello)
        with open(hello, 'r+', encoding="ISO-8859-1") as f:
            text = f.readlines()
            for i in range(len(text)):
                fout = open("./timestamps.txt", "a",encoding="ISO-8859-1")
                fout.write(text[i])
    except FileNotFoundError:
        pass
