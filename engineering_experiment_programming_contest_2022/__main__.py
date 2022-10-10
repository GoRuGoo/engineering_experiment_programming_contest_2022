
import cv2
from deepface import DeepFace

from modules.sound import make_sound
from modules.useful_servo import UsefulServoClass
import sys
sys.path.appen('/usr/local/lib/python3.7/dist-packages')

cap = cv2.VideoCapture(0)
judge_sad_nutral = False
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
                servo_instance.move_servo(90, 1.0)
                servo_instance.move_servo(-90, 1.0)
                make_sound("suisei_amayakasi_trim.wav")


if __name__ == "__main__":
    main()