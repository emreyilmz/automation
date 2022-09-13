# 5 - delete subtitle line:20% -->(-to)
import re

import os
directories_in_curdir = list(filter(os.path.isdir, os.listdir(os.curdir)))
for a in directories_in_curdir:
    with open('./'+a+'/subtitle.vtt', 'r+') as f:
        file = f.read()
        file = re.sub(r"line:20%", "", file, flags=re.MULTILINE)
        file = re.sub(r"-->", "-to", file, flags=re.MULTILINE)
        fout = open("./"+a+"/subtitle.vtt", "w+")
        fout.write(file)
        print(file)
