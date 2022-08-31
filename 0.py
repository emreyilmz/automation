from da import Channel 
from da import YouTube

 
 
def main(): 
    
    c = Channel("https://www.youtube.com/c/whitehouse45/videos") 
    number = 0
    for url in c.video_urls: 
        yt = YouTube('https://www.youtube.com/watch?v='+url)
        y = str(yt.captions) 
        #hello = yt.captions
        index = y.find('<Caption lang="English" code="en">')
        if index == 7:
            print(url)
       
        
        
 
 
if __name__ == '__main__': 
    main() 