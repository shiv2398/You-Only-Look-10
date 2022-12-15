import cv2
import os
def image_generator(path,person_name):
    """image_generator(path,person_name)"""
    cam = cv2.VideoCapture(path+'/'+person_name+'.avi')
    currentframe = 0
    i=0
    while(True):
        ret,frame = cam.read()
        
        if ret:
            name = path+'/'+'image(' + str(currentframe) + ').jpg'
            
            cv2.imwrite(name, frame)
            currentframe += 1
            i+=1
        if i==100:
            break
        else:
            break
    os.remove(path+'/'+person_name+'.avi')
    cam.release()
    cv2.destroyAllWindows()
    print(f'{i}:Image are Generated')