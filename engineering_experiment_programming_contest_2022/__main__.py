import sys

import cv2
from deepface import DeepFace

from .modules.sound import make_sound
from .modules.useful_servo import UsefulServoClass

cap = cv2.VideoCapture(0)
servo_instance = UsefulServoClass()
servo_instance.set_gpio(13)


def main():
    while True:
        ret, frame = cap.read()
        if frame.size != 0:
            result_ = DeepFace.analyze(frame, actions=["emotion"])
            cv2.imshow("FACE", frame)
            if result_["dominant_emotion"] == "sad":
                cap.release()
                cv2.destroyAllWindows(0)
                servo_instance.move_many_times_servo()
                make_sound("suisei_amayakasi_trim.wav")
                sys.exit()


if __name__ == "__main__":
    main()
