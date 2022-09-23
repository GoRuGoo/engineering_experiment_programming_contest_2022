import cv2


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()
    print(frame.size)

    cv2.imshow("frame",frame)


    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cv2.destroyAllWindows()