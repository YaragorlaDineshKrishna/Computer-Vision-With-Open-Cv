import cv2
import numpy as np
cap = cv2.VideoCapture("C://Users//ramak//Videos//Movies//Passengers (2016) 720p BDRip Multi Audios.mkv")
if (cap.isOpened()== False):
    print("Error opening video file")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
