#This will open a camera and click the picture

import cv2
cap=cv2.VideoCapture(0)
status, photo = cap.read()
print(status)
cv2.imshow('my photo',photo)
cv2.waitKey(10000)
cv2.destroyAllWindows()
cap.release()
