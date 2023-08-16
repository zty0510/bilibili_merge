import os
import subprocess    
import json
current_dir = os.getcwd()
files = os.listdir(current_dir)
# print(current_dir)
for root, dirs, files in os.walk(current_dir):
    # print(files)
    if '.videoInfo' in files:
        with open(root+'\.videoInfo', 'rb') as f:
            videoInfo_json = json.load(f)
        files = list(filter(lambda x: x.endswith('.mp4'), files))
        # print(files)
        input_file1 = root+'\\'+files[0]
        input_file2 = root+'\\'+files[1]
        output_file = root+'\\'+videoInfo_json['title']+'.mp4'

        print(output_file)
        codec = 'copy'
        subprocess.run(f"ffmpeg -i {input_file1} -i {input_file2} -c {codec} {output_file}")
# ffmpeg -i "1050618664-1-30280.mp4" -i "1050618664-1-30120.mp4" -c copy "output.mp4"
