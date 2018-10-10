
# Author - Shubham Nikam

# Script to convert image from BGR to HSV (Hue = 0-180,Saturation = 0-255,Value = 0-255)

import cv2

img = cv2.imread('baboon.png')

cv2.imshow('Baboon_Image',img)
cv2.waitKey(0)

hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('HSV Image',hsv_img)
cv2.imshow('Hue Channel',hsv_img[:,:,0])
cv2.imshow('Saturation Channel',hsv_img[:,:,1])
cv2.imshow('Value Channel',hsv_img[:,:,2])
cv2.waitKey(0)

cv2.destroyAllWindows()
