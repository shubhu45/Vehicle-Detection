# Author- Shubham Nikam

# Script to read and write image in OpenCV

import cv2

img=cv2.imread('baboon.png')

cv2.imshow('Baboon',img)
cv2.imwrite('baboon.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()