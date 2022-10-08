import sys
import threading

import cv2
from deepface import DeepFace

from .modules.sound import make_sound
from .modules.useful_servo import UsefulServoClass

cap = cv2.VideoCapture(0)
judge_sad_nutral = False


def move_servo():
    servo_instance = UsefulServoClass()
    servo_instance.set_gpio(13)
    while True:
        servo_instance.move_servo(90, 1.0)
        servo_instance.move_servo(-90, 1.0)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            sys.exit()


def sound_suisei():
    make_sound("../suisei_amayakasi_trim.wav")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        sys.exit()


thread_servo = threading.Thread(target=move_servo)
thread_suisei = threading.Thread(target=sound_suisei)


def main():
    while True:
        ret, frame = cap.read()
        if frame.size != 0:
            result_ = DeepFace.analyze(frame, actions=["emotion"])
            cv2.imshow("FACE", frame)
            if result_["dominant_emotion"] == "sad":
                del DeepFace
                # DeepFaceクラス内で顔検出されなかったらsys.exitの処理が入っている
                # これでは使い勝手が悪いので強制的にインスタンス(?)を削除しておく
                cap.release()
                break
        thread_servo.start()
        thread_suisei.start()
