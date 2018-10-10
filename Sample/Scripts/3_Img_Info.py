
# Author - Shubham Nikam

# Script to get Image Information

import cv2

img = cv2.imread('baboon.png')

cv2.imshow('Baboon_Image',img)

print img.shape

print "\n Height pixel Values :- ",img.shape[0]
print "\n Width pixel Values :- ",img.shape[1]
print "\n ",img.dtype
print "\n ",type(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
