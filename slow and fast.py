import cv2
import numpy as np

cap = cv2.VideoCapture("//Mac/Home/Downloads/Movies/Stranger things S04/sts0401.mkv")

if not cap.isOpened():
    print("Error opening video file")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Frame', frame)
        if cv2.waitKey(250) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
