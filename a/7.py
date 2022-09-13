# 8 - numbers extract

import os
directories_in_curdir = list(filter(os.path.isdir, os.listdir(os.curdir)))
for a in directories_in_curdir:
    with open("./"+a+"/timestamps.vtt", 'r', encoding='utf-8') as f:
        text = f.readlines()
        
        for i in range(len(text)):
            #print("0x"+a+"y"+str(i))
            hello = "0x"+a+"y"+str(i+1)
            fout = open("./"+a+"/numbers.vtt", "a")
            fout.write(hello+"\n")
