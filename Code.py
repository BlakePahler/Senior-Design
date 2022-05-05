import cv2
import numpy as np
import time

time.sleep(20)

# Connect to webcam
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)
cap3 = cv2.VideoCapture(4)

#These resolutions work with this refresh rate
cap1.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap1.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

cap3.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap3.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    
    cv2.imshow('Webcam1', frame1)
    cv2.imshow('Webcam2', frame2)
    cv2.imshow('Webcam3', frame3)
    
    # Opens cameras as follows:
    #   center
    # Left-Right
      
    # cv2.moveWindow('Webcam1', 320, 545)
    # cv2.moveWindow('Webcam2', 640, 0)
    # cv2.moveWindow('Webcam3', 960, 545)

    #Opens cameras left-center-right
    cv2.moveWindow('Webcam1', 0, 320)
    cv2.moveWindow('Webcam2', 640, 320)
    cv2.moveWindow('Webcam3', 1280, 320)
    
    # Checks if q is hit and ends loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()
