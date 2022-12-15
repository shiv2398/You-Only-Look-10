import cv2 as cv
import os 
import numpy as np
import time
import imgaug as ia
from imgaug import augmenters as iaa
import os
import sys
import argparse
from glob import glob
import cv2
import shutil
import random
from PIL import Image
import pandas as pd
import errno
def data_agumentation(path,n):
    """data_agumentation->(path_dir,Number of images Agunetation)"""
    IMG_DIR=path
    if not os.path.isdir(IMG_DIR):
        print('%s is not a valid directory.' % IMG_DIR)
        sys.exit(1)
    IMG_EXTENSION = '.jpg'
    NUM_AUG_IMAGES = n
    cwd = os.getcwd()
    seq1 = iaa.Sequential([
        iaa.Fliplr(0.5),                             # Horizontal flip 50% of images
        iaa.Crop(percent=(0, 0.10)),                 # Crop all images between 0% to 10%
        iaa.GaussianBlur(sigma=(0, 1)),              # Add slight blur to images
        ])
    img_fns = glob(IMG_DIR + '/*' + IMG_EXTENSION)
    count=0
    for img_fn in img_fns:
        img1_bgr = cv2.imread(img_fn) # Load image with OpenCV
        img1 = cv2.cvtColor(img1_bgr, cv2.COLOR_BGR2RGB) # Re-color to RGB from BGR
        for i in range(NUM_AUG_IMAGES):
            img_aug1 = seq1(images=[img1])[0] # Apply augmentation to image
            base_fn = img_fn.replace(IMG_EXTENSION,'') # Get image base filename
            img_aug_fn = base_fn + ('_aug%d' % (i+1)) + IMG_EXTENSION # Append "aug#" to filename
            img_aug_bgr1 = cv2.cvtColor(img_aug1, cv2.COLOR_RGB2BGR) # Re-color to BGR from RGB
            cv2.imwrite(img_aug_fn,img_aug_bgr1) # Save image to disk
            count+=1
    print(f'Image Agumentation successfully Done !! {count} images Agumented')