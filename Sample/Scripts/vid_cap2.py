#Author - Saurav Gore

#Playing video from a video file

import cv2
import numpy as np
from matplotlib import pyplot as plt

sg_cap = cv2.VideoCapture("/home/hduser/opencv/pro/vid/Episode (1).mkv")

while sg_cap.isOpened():
	ret,frame = sg_cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',gray)
    	if cv2.waitKey(1) & 0xFF == ord('q'):  #0xFF is used 64 bit machine
        	break

sg_cap.release()
cv2.destroyAllWindows()
