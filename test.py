import os 
import pickle
import cv2
import matplotlib.pyplot as plt
import json
main_dir='/media/sahitya/OS/10_sec'
for root, dirs, files in os.walk(main_dir):
    for file in files:
        if file.endswith('.json'):
            data_file=file
            file_path=os.path.join(main_dir,data_file) 
    
def test_image(path):
    f = open (file_path, "r")
    classes=json.loads(f.read())

    img=cv2.imread(path)
    img_r=cv2.resize(img,(48,48))
    image=img_r.reshape(1,-1)
    with open('/media/sahitya/OS/10_sec/best_models/best_model.pkl', 'rb') as f:
        model = pickle.load(f)
    y_pred=model.predict(image)
    for key,value in classes.items():
        if value==int(y_pred):
            pred_class=key
    plt.imshow(img_r)
    plt.title(f'Class : {pred_class},Label{int(y_pred)}')
    plt.show()
    
            
