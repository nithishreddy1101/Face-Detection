import cv2 as cv
import numpy as np 

img =cv.imread("File path") #for example img =cv.imread("Photos\\group.jpeg")

cv.imshow("File Name(random)",img)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

haar_cascade=cv.CascadeClassifier('haarcascade_frontalface_default.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)
cv.imshow("Detected Images",img)
print(f'No. of faces ={len(faces_rect)}')

cv.waitKey(0)
