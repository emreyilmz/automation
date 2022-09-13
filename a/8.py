import os
directories_in_curdir = list(filter(os.path.isdir, os.listdir(os.curdir)))
for a in directories_in_curdir:
    with open("./"+a+"/timestamps.vtt", 'r', encoding='utf-8') as f:
        text = f.readlines()
        
        for i in range(len(text)):
            #i=i+1
            #print(text[i])
            text2=text[i].rstrip('\n').split(',')
            #print(text2[0])
            os.system(
                "ffmpeg -ss "+text2[0]+" -i ./"+a+"/video.mkv -reset_timestamps 1 -acodec libmp3lame -vcodec libx264 -avoid_negative_ts make_zero ./"+a+"/0x"+a+"y"+str(i)+".mp4"
            )
            #ffmpeg -ss "+text2[0]+" -i ./"+a+"/video.mkv -reset_timestamps 1 -acodec libmp3lame -vcodec libx264 -avoid_negative_ts make_zero ./"+a+"/0x"+a+"y"+str(i)+".mp4
