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

def video_generator(path,person_name):  
    """" video_generator('path,person_name)"""
    video = cv2.VideoCapture(0)
    if (video.isOpened() == False): 
        print("Error reading video file")
    frame_width = int(video.get(3))
    frame_height = int(video.get(4))
    size = (frame_width, frame_height)
    result = cv2.VideoWriter(path+'/'+person_name+'.avi', 
                             cv2.VideoWriter_fourcc(*'MJPG'),
                             10, size)
    capture_duration = 10
    start_time = time.time()
    while(int(time.time() - start_time) < capture_duration):
        ret, frame = video.read()
        if ret == True: 
            result.write(frame)
            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else:
            break
    video.release()
    result.release()
    cv2.destroyAllWindows()
    print("The video was successfully saved")