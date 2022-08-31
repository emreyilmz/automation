import re

import os
directories_in_curdir = list(filter(os.path.isdir, os.listdir(os.curdir)))
for a in directories_in_curdir:
    with open('./3/subtitle.vtt', 'r+') as f:
        file = f.read()

        # find the DATA_TO_MATCH
        file = re.sub(r"line:20%", "", file, flags=re.MULTILINE)

        # find the DATA_CATCHME
        #file = re.sub(r"?<=[a-z])\r?\n", "", file, flags=re.MULTILINE)
        file = re.sub(r"-->", "-to", file, flags=re.MULTILINE)


        print(file)
        fout = open("./3/subtitle.vtt", "w+")
        fout.write(file)
