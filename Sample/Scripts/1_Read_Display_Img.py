
# Author - Shubham Nikam

# Basic Program of Displaying image

import cv2

img = cv2.imread('baboon.png')

cv2.imshow('Baboon_Image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
