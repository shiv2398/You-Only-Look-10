import os 
import json
main_dir='/media/sahitya/OS/10_sec'
for root, dirs, files in os.walk(main_dir):
    for file in files:
        if file.endswith('.json'):
            data_file=file
            file_path=os.path.join(main_dir,data_file) 
    

f = open (file_path, "r")
classes=json.loads(f.read())
for key,item in classes.items():
    print(key,item)