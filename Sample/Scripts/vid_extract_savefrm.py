#Author - Saurav Gore

#Extracting and Saving Video Frames

import cv2
import numpy as np
from matplotlib import pyplot as plt

sg_cap = cv2.VideoCapture("/home/hduser/opencv/pro/vid/Episode (1).mkv")
x,img = sg_cap.read()
cnt = 0
x = True
while x:
	ret,frame = sg_cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	cv2.imwrite("/home/hduser/opencv/pro/vid/vid_frames/frame%d.jpg" % cnt,img)
	x,img = sg_cap.read()
	print "Read a new frame:   " , x
	cv2.imshow('frame',gray)
	#cv2.imshow('frame',hsv)
	cnt+=1
    	if cnt == 1000:         				#break after 1000 frames
        	break

sg_cap.release()
cv2.destroyAllWindows()
