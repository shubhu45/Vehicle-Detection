# Author - Shubham Nikam

# Script for blurring the images

import cv2
import numpy as np

img = cv2.imread('baboon.png')

cv2.imshow('Baboon Image',img)
cv2.waitKey(0)

#create 3x3 kernel
kernel_3x3=np.ones((3,3),np.float32)/9

#using cv2.filter2D for blurring
blurred=cv2.filter2D(img,-1,kernel_3x3)

cv2.imshow('Kernel Blurred Image 1',blurred)
cv2.waitKey(0)

kernel_7x7=np.ones((7,7),np.float32)/49
blurred1=cv2.filter2D(img,-1,kernel_7x7)
cv2.imshow('Kernel Blurred Image 2',blurred1)
cv2.waitKey(0)

#using boxFilter or blur
blur=cv2.blur(img,(7,7))
cv2.imshow('Blur Filter',blur)

#using Gaussian Filter
gaussian=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('Gaussian Filter',gaussian)

#using medianBlur
median=cv2.medianBlur(img,7)
cv2.imshow('Median Blur Image',median)

#using bilateralFilter most effective in noise removal
bilateral=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral Filtering',bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()