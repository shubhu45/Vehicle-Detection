
# Author - Shubham Nikam

# Script for detecting car object

import cv2

# capture frames from a video
cap = cv2.VideoCapture(0)

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    # reads frames from a video
    ret, frames = cap.read()

    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)

    # Detects cars of different sizes in the input image
    cars = car_cascade.detectMultiScale(gray,1.1,1)

    # To draw a rectangle in each cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frames,(x, y),(x + w, y + h),(255,0,0),2)

    # Display frames in a window
    cv2.imshow('Cars Detection',frames)

    if cv2.waitKey(33) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()