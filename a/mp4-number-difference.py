import os
import sys

walk_dir = "./"

print('walk_dir = ' + walk_dir)
total=0
for root, subdirs, files in os.walk(walk_dir):
    try:
        dir_path = root+"/"
        hello = root+'/text.txt'
    #print(hello)
        count = 0
        for path in os.scandir(dir_path):
            if path.is_file():
                count += 1
    
        with open(hello, 'r+', encoding="ISO-8859-1") as f:
            text = f.readlines()
            countt = len(text)
        #print(dir_path+':', count-5)
        de = count-5
        #print(hello+':', countt)
        if countt!=de:
            print(dir_path)
            print(hello+':', countt)
            print(dir_path+':', count-5)
    except FileNotFoundError:
        pass 
