# Author - Shubham Nikam

# Script for detecting edges in Images

import cv2

# for edge detection we require image in gray scale
img = cv2.imread('baboon.png',0)

cv2.imshow('Baboon Image',img)
cv2.waitKey(0)

height,width=img.shape[:2]

# Using Sobel
sobel_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

cv2.imshow('Sobel_x',sobel_x)
cv2.imshow('Sobel_y',sobel_y)

sobel_OR=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('Sobel OR Image',sobel_OR)
cv2.waitKey(0)

# Laplacian edge detection
lap=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('Laplacian Image',lap)
cv2.waitKey(0)

# Using Canny Edge Detection (It uses gradient values as thresholds)
canny=cv2.Canny(img,2,180)
cv2.imshow('Canny Edge Detection',canny)
cv2.waitKey(0)

cv2.destroyAllWindows()