#Author - Saurav Gore

#Saving video from a video file

import numpy as np
import cv2
from matplotlib import pyplot as plt

sg_cap = cv2.VideoCapture("/home/hduser/opencv/pro/vid/Episode (1).mkv")

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('/home/hduser/opencv/pro/vid/video2_out.mkv',fourcc, 20.0, (640,480))

while(sg_cap.isOpened()):
    ret, frame = sg_cap.read()
    #bgr = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    if ret == True:
        frame = cv2.flip(frame,0)
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

sg_cap.release()
out.release()
cv2.destroyAllWindows()
