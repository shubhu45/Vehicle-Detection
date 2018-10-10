# Author - Shubham Nikam

# Script to translate image using Warpaffine

import cv2
import numpy as np

img=cv2.imread('baboon.png')

cv2.imshow('Baboon Image',img)
cv2.waitKey(0)

# storing height and width of image

height,width=img.shape[:2]

print height
print width

q_height,q_width=height/4,width/4

print q_height
print q_width


# Using Translation Matrix T

T=np.float32([[1,0,q_width],[0,1,q_height]])
print T

# Using WarpAffine Translation

img_traslated=cv2.warpAffine(img,T,(width,height))
cv2.imshow('Translated Image',img_traslated)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Image Rotation using Transpose Concept

rotated_img=cv2.transpose(img)

cv2.imshow('Original Image',img)
cv2.imshow('Rotated Image',rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


