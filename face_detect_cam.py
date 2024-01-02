import cv2 as cv 


capture=cv.VideoCapture(0) #0 for webcam 1 for first cam and 2 for 2nd cam connected
haar_cascade=cv.CascadeClassifier('C:\\Users\\nithi\\AppData\\Roaming\\Python\\Python312\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
while True:
    isTrue,frame =capture.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
    for (x,y,w,h) in faces_rect:
        
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
    cv.imshow("Video",frame)
    print(f'The no. of faces found are {len(faces_rect)}')
    if cv.waitKey(20) & 0xFF==ord("d"):
        break
capture.release()
cv.destroyAllWindows()