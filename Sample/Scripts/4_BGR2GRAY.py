
# Author - Shubham Nikam

# Script to convert image from BGR to Gray

import cv2

img = cv2.imread('baboon.png')

cv2.imshow('Baboon Image',img)
cv2.waitKey(0)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Scale Image",gray_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
