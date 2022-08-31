import re
import os
#print("\nWe are listing out only the directories in current directory -")
directories_in_curdir = list(filter(os.path.isdir, os.listdir(os.curdir)))
#print(type(directories_in_curdir))

pattern = r'(\d{2}:\d{2}:\d{2},d{3}$)|(\d{2}:\d{2}:\d{2})'
for a in directories_in_curdir:
    with open("./"+a+"/subtitle.vtt", 'r', encoding='utf-8') as f:
        text = f.readlines()
        for i in range(len(text)):
            if re.match(pattern, text[i]):
                print(text[i])
                fout = open("./"+a+"/timestamps.vtt", "a")
                fout.write(text[i])