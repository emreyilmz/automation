# 8 - numbers extract

import os
directories_in_curdir = list(filter(os.path.isdir, os.listdir(os.curdir)))
for a in directories_in_curdir:
  try:
        os.remove("./"+a+"/numbers.txt")


            
            
  except FileNotFoundError:
    pass
