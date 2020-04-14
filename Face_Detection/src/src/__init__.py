import numpy as np
import cv2
from cv2 import cvtColor
from PIL import ImageGrab
import win32gui
import time
import serial

arduino = serial.Serial('com3',9600, timeout = 0.3)
casc = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_default.xml')
side_casc = cv2.CascadeClassifier('cascades/data/haarcascade_profileface.xml')

templist = []
otherlist = []
def send_directions(direction):
    if direction == "left":
        arduino.write('1')
    elif directon == "right":
        arduino.write('2')
    else:
        arduino.write('3')

def enum_win(hwnd, result):
    #print(hwnd)
    
    winText = win32gui.GetWindowText(hwnd)
    
    #print(winText)
    
    otherlist.append((hwnd,winText))
    
def getDirections(xcords):
    if xcords > 380:
        
        return ("right")
    elif xcords < 250:
        return ("left")
    else:
        return ("center")

dirfr = ""
dirf = ""
dirs = ""

win32gui.EnumWindows(enum_win, templist)

screen_hwnd = 0
for (hwnd,winText) in otherlist:
        if "GStreamer" in winText:
            screen_hwnd = hwnd
        
start, end = 0,0    
while(True):   
    #start = int(round(time.time() * 1000)) # <---------------------
    
    winPos = win32gui.GetWindowRect(screen_hwnd)
    
    cap = np.array(ImageGrab.grab(winPos))
    
    #declare frame    
    frame = cvtColor(cap, cv2.COLOR_RGB2BGR)
    
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
        nx = (2 * h) - x 
        # formula for calculating x that has been flipped over a vertical line        
        cv2.rectangle(frame,(nx,y),(nx + w,y + h),(0,0,255),2)
         
        #block of code to not spam current location of face 
        dotPos = nx + (w//2)
        dir1 = getDirections(dotPos)
         
        if dir1 == dirfr:
            continue
        else:
            dirfr = dir1
            send_directions(dirFr)
            print(dirfr)
             
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x + w,y + h),(255,0,0),2)
         
        dotPos = x + (w//2)
        dir1 = getDirections(dotPos)
         
        if dir1 == dirf:
            continue
        else:
            dirf = dir1
            send_directions(dirf)
            print (dirf)
         
         
    for (x,y,w,h) in side:
        cv2.rectangle(frame,(x,y),(x + w,y + h),(0,255,0),2)
         
        dotPos = x + (w//2)
        dir1 = getDirections(dotPos)
         
        if dir1 == dirs:
            continue
        else:
            dirs = dir1
            send_directions(dirs)
            print (dirs)
    #shows window
    cv2.imshow('output', frame)
    
    
    #press q to close window
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
    
    #end = int(round(time.time() * 1000)) # <--------------------
    print(end - start)
cv2.destroyAllWindows()
