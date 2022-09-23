
import cv2
from deepface import DeepFace
import numpy as np


cap = cv2.VideoCapture(0)

while True :
    ret, frame = cap.read()
    if(frame.size!=0):
        result_ = DeepFace.analyze(frame,actions=['emotion'])
        cv2.imshow('frame',frame)
        print(result_["dominant_emotion"])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:print("test")

cap.release()
cv2.destroyAllWindows()