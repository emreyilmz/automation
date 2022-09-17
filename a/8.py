import os
directories_in_curdir = list(filter(os.path.isdir, os.listdir(os.curdir)))
for a in directories_in_curdir:
    try:
        a=int(a)+17
        a=str(a)
        with open("./"+a+"/timestamps.txt", 'r', encoding='utf-8') as f:

            print(a)
            text = f.readlines()
        
            for i in range(len(text)):
                c = str(i)
                hello ="./"+a+"/0x"+a+"y"+str(i)+".mp4"
                file_exists = os.path.exists(hello)
                if file_exists :
                    print("file exists")
                else:
                    text2=text[i].rstrip('\n').split(',')
                    os.system(
                        "ffmpeg -ss "+text2[0]+" -i ./"+a+"/video.mkv -reset_timestamps 1 -acodec libmp3lame -vcodec libx264 -avoid_negative_ts make_zero ./"+a+"/0x"+a+"y"+str(i)+".mp4"
                    )
    except FileNotFoundError:
        pass
