import os
import json
current_dir = os.getcwd()
for root, dirs, files in os.walk(current_dir):
    files = os.listdir(root)
    print(files)
    if '.videoInfo' in files:
      # print("ok")
      with open(root+'\.videoInfo', 'rb') as f:
        videoInfo_json = json.load(f)
        print(videoInfo_json)
        files = filter(lambda x: x.endswith('.mp4'), files)
        for id, file in enumerate(files):
            os.rename(root+'\\'+file, root+'\\'+videoInfo_json['title']+str(id)+'.mp4')
            
            