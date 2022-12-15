
from keras.models import load_model
import os
import cv2
import numpy as np
from os import listdir
from os.path import isfile,join
import re
import cv2
import numpy as np
from time import sleep
from tensorflow.keras.utils import img_to_array
import streamlit as st
import keras

import cv2
import numpy as np
from time import sleep

face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def face_detector(img):
    gray=cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY)
    faces=face_classifier.detectMultiScale(gray,1.3,5)
    if faces is ():
        return (0,0,0,0),np.zeros((48,48),np.uint8),img
    allfaces=[]
    rects=[]
    for (x,y,w,h) in faces:
        x=x-50
        w=w+50
        y=y-50
        h=h-50
        cv2.rectangle(img,(x,y),(x+w,y+w),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
    try:
        roi_gray=cv2.resize(roi_gray,(48,48),interpolation=ccv2.INTER_AREA)
    except: 
        return (x,w,y,h),np.zeros((48,48),np.uint8),img
    return (x,y,w,h),roi_gray,img
    
classifier= keras.models.load_model("model.h5")
face_classifier=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
class_labels={
    0:'shiv',
    1:'vasu'
            }
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    rect,face,image=face_detector(frame)
    if np.sum([face])!=0.0:
        roi=face.astype('float')/255.0
        roi=img_to_array(roi)
        
        roi=np.expand_dims(roi,axis=0)
        
        preds=classifier.predict((roi)[0])
        
        label=class_labels[preds.argmax()]
        
        label_position=(rect[0]+int((rect[1]/2)),rect[2]+25)
        cv2.putText(image,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
    else:
        cv2.putText(image,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
    
    cv2.imshow('All',image)
    if cv2.waitKey(1)==13:
        break
        
cap.release()
cv2.destroyAllWindows()