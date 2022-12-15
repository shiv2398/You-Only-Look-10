import os 
import streamlit as st
from data_generator_prep import prep
from Data_processing import split
from models import clf
from train import *
import cv2
from test import test_image
main_dir='/media/sahitya/OS/10_sec'
csv_path='/media/sahitya/OS/10_sec/csv_data'
for root, dirs, files in os.walk(csv_path):
    for file in files:
        if file.endswith('.csv'):
            data_file=file
            global path
            path=os.path.join(csv_path,data_file) 
def main():
  
    d_c=input('Data Generate(yes/no) : ')
    if d_c=='yes':
        prep()
        print('\n\nData prepartion Complete')
    x_train,x_test,y_train,y_test=split(path)
    print('\n\nData Preprocessing---------->data(splitted)')
    print((f'\n\nShape x_train:{x_train.shape},y_train:{x_test.shape}'))
    print('\n\nModel training-------------------------------------------------')
    m=train_model(path)
    print('\n\nTraining Complete-----------------------------------------------------')
    if m==1:
        inputt=input('\n\nTest Model(yes/no) :')
        if inputt=='yes':
            image_path=input('\n\nEnter image path(yes/no) : ')
            test_image(image_path)
        print('\n\n*******************************Testing Complete*******************************')
    else:
        print('Model not saved----(No Testing )')
if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()


    


    


           