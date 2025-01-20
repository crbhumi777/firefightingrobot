import cv2,os   #opencv library 
import shutil   # shutil module offers a number of high-level operations on files and collections of files
#This module helps in automating process of copying and removal of files and directories.
import numpy as np   #scientific computing
import os

#Tracking images
def TrackImages():
    #Local Binary Patterns Histograms for face recognization
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    #save Haar Cascade file
    harcascadePath = "./haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    #capture video
    cam = cv2.VideoCapture(0)
    cam.set(3,426)
    cam.set(4,240)
    font = cv2.FONT_HERSHEY_SIMPLEX           
    while True:

        #read images
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        #M   
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    

        for(x,y,w,h) in faces:

            #draw bounding box
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)                                             
            cv2.putText(im,"Humen Detected",(x,y+h), font, 1,(255,255,255),2)            
        cv2.imshow('im',im)
        if (cv2.waitKey(1)==ord('q')):
            cam.release()
            cv2.destroyAllWindows()
            break
