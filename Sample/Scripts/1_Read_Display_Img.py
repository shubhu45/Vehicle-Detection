
# Author - Shubham Nikam

# Script to Read and Display image

import cv2

img = cv2.imread('baboon.png')

cv2.imshow('Baboon Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
