# Author- Shubham Nikam

# Script to read and write image in OpenCV

import cv2

img=cv2.imread('/home/elasticsearch/Vehicle Detection/Sample/Images/baboon.png')

cv2.imshow('baboon Image',img)
cv2.imwrite('/home/elasticsearch/Vehicle Detection/Sample/Images/baboon.jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
