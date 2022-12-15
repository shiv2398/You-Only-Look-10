import os 
from PIL import Image
def image_rescaling(path,width=48,height=48):
    """image_rescaling->(path of image_dir)"""
    for img in os.listdir(path):
        img_dir=os.path.join(path,img)
        img = Image.open(img_dir)
        img = img.resize((width, height)) 
        img.save(img_dir)
    print('image_rescaled')