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

for instrument in instruments_list:
    instrument_video_ids= list(data['videos'][instrument])
    for id in instrument_video_ids:
        print(id)
        video_url= 'https://www.youtube.com/watch?v='+id

        try:
            print("url",video_url)
            youtube = pytube.YouTube(video_url)
            video = youtube.streams.first()
            print("downloading")
            video.download('data/as/')
            print("finished downloading")
        except pytube.exceptions.VideoUnavailable:
            print ("unavailable")
        except pytube.exceptions.RegexMatchError:
            print ("regex error")
        except pytube.exceptions.ExtractError:
            print("extract error")
