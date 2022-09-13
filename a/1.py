# 1 - download videos (ind)

from __future__ import unicode_literals
from os import lseek
import yt_dlp
with open("links.txt") as f,open("output.txt","w") as out:
    lines = f.readlines()
    for ind,line in enumerate(lines):
       ydl_opts = {
        'outtmpl': '/'+str(ind+100)+'/video',
        'format': '(bestvideo[width>=480][ext=mp4]/bestvideo)+bestaudio/best',
        'writesubtitles': True,
        'subtitle': '--write-sub --sub-lang en',
        }
       url = line
       with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
       print("Download Successful!")


