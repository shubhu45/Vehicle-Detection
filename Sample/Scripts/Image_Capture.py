# Author - Shubham Nikam

# Script to capture image using webcam

import cv2
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)

if cap.isOpened():
    ret,frame=cap.read()
    print ret
    print frame
else:
    ret=False

img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

plt.imshow(img)
plt.title("Captured Image")
plt.xticks([])
plt.yticks([])
plt.show()

cap.release()
cv2.destroyAllWindows()
