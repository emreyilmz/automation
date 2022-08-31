#rename subtitle files

import shutil
import os
directories_in_curdir = list(filter(os.path.isdir, os.listdir(os.curdir)))
for a in directories_in_curdir:
    try:
        shutil.move('./'+a+'/video.en-US.vtt', './'+a+'/subtitle.vtt')
    except FileNotFoundError:
        pass
    try:
        shutil.move('./'+a+'/video.en.vtt', './'+a+'/subtitle.vtt')
    except FileNotFoundError:
        pass