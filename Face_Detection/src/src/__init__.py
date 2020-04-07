import numpy as np
import cv2


casc = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
side_casc = cv2.CascadeClassifier('cascades/data/haarcascade_profileface.xml')


def getDirections(xcords):
    if xcords > 380:
        return ("right")
    elif xcords < 250:
        return ("left")
    else:
        return ("center")
    
cap = cv2.VideoCapture(0)

dirfr = ""
dirf = ""
dirs = ""
while(True):
    #declare frame
    ret, frame = cap.read()
    
    # inverted frame to capture side profile
    frame2 = cv2.flip(frame, 1)
    
    # set up gray scale variable 
    gs = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # gray scale for inverted frame of side profile
    flipgs = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    #front facing cascade
    faces  = casc.detectMultiScale(gs, scaleFactor=1.5,minNeighbors=5)
    
    # inverted side cascade
    face_right = side_casc.detectMultiScale(flipgs, scaleFactor=1.5,minNeighbors=5)
    
    # side cascade 
    side = side_casc.detectMultiScale(gs, scaleFactor=1.5,minNeighbors=5)
    
    # loop for drawing box around faces detected on a side profile
    for (x,y,w,h) in face_right:
        
        # calculating x since the frame the faces being detected have been flipped
        nx = 2 * h - x 
        # formula for calculating x that has been flipped over a vertical line
        
        cv2.circle(frame,(nx + (w//2),y + (h//2)), 4,(0,0,255), -2)
        #getting the center of each rectangle shown around a face
        
        cv2.rectangle(frame,(nx,y),(nx + w,y + h),(0,0,255),2)
        
        #block of code to not spam current location of face 
        dotPos = nx + (w//2)
        dir1 = getDirections(dotPos)
        
        if dir1 == dirfr:
            continue
        else:
            dirfr = dir1
            print (dirfr)
            
    for (x,y,w,h) in faces:
        
        cv2.circle(frame,(x + (w//2),y + (h//2)), 4,(0,0,255), -2)
        cv2.rectangle(frame,(x,y),(x + w,y + h),(255,0,0),2)
        
        dotPos = x + (w//2)
        dir1 = getDirections(dotPos)
        
        if dir1 == dirf:
            continue
        else:
            dirf = dir1
            print (dirf)
        
        
    for (x,y,w,h) in side:
        cv2.circle(frame,(x + (w//2),y + (h//2)), 4,(0,0,255), -2)
        cv2.rectangle(frame,(x,y),(x + w,y + h),(0,255,0),2)
        
        dotPos = x + (w//2)
        dir1 = getDirections(dotPos)
        
        if dir1 == dirs:
            continue
        else:
            dirs = dir1
            print (dirs)
    #shows window
    cv2.imshow('output', frame)
    
    
    #press q to close window
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
