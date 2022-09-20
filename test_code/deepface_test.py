from unittest import result
import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

while cap.isOpened() :
    ret, frame = cap.read()
    result = DeepFace.analyze(frame,actions=['emotion'])
    cv2.imshow('frame',frame)
    print(result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()