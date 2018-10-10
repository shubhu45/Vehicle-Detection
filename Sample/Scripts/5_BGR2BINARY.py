
# Author - Shubham Nikam

# Script to convert image from BGR to Binary

import cv2

img = cv2.imread('baboon.png')

cv2.imshow('Baboon_Image',img)
cv2.waitKey(0)

gray_img=cv2.imread('baboon.png',0)
cv2.imshow('Gray Scale Image',gray_img)
cv2.waitKey(0)

ret,binary_img=cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
cv2.imshow('Binary Image',binary_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
