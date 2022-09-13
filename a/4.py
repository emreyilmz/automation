# 4 - subtitle extract
import pysrt
import os
#print("\nWe are listing out only the directories in current directory -")
directories_in_curdir = list(filter(os.path.isdir, os.listdir(os.curdir)))
#print(type(directories_in_curdir))

for a in directories_in_curdir:
    subs = pysrt.open("./"+a+"/subtitle.vtt")
    for sub in subs:
        #print(sub.text)
        fout = open("./"+a+"/subtitle.txt", "a")
        fout.write(sub.text+"\n")
