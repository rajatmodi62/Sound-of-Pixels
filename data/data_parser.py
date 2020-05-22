import os
import math
import shutil as sh
from pathlib import Path
import json
import pytube
import pytube.exceptions
local_data_path = Path('.').absolute()

json_path="./MUSIC_solo_videos.json"
# json_path="./MUSIC_duet_videos.json"


f = open(json_path)
data = json.load(f)
#print(type(data),len(data),data.keys(),type(data['videos']),data['videos'].keys())

#instruments list
instruments_list= list(data['videos'].keys())
total_videos=0
for instrument in instruments_list:
    instrument_video_ids= list(data['videos'][instrument])
    for id in instrument_video_ids:
        total_videos+=1

error_list=[]
count=0
for instrument in instruments_list:
    instrument_video_ids= list(data['videos'][instrument])

    for id in instrument_video_ids:
        print(id)
        video_url= 'https://www.youtube.com/watch?v='+id
        count+=1
        print("Processed Video: ",count, " out of",total_videos," videos")
        try:
            #print("url",video_url)
            youtube = pytube.YouTube(video_url)
            video = youtube.streams.first()
            print("downloading")
            dump_path= 'data/'+ str(instrument)+ '/'
            print("dump path is",dump_path)
            video.download(dump_path,filename=id)
            print("finished downloading")

        except pytube.exceptions.VideoUnavailable:
            print ("unavailable")
            error_list.append(video_url)

        except pytube.exceptions.RegexMatchError:
            print ("regex error")
            error_list.append(video_url)

        except pytube.exceptions.ExtractError:
            print("extract error")
            error_list.append(video_url)


with open('errors.txt', 'w') as f:
    f.writelines("%s\n" % error for error in error_list)
