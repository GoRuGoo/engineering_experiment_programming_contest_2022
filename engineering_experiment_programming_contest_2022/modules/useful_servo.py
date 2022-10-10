import time

import sg90
import wiringpi


class UsefulServoClass:
    def set_gpio(self, pin_num: int) -> None:
        """Setting up the gyro. initializeを使ってピン番号のセットアップしても良かったが、
        毎回インスタンス建て替えないといけないのでメソッド化した。

        Args:
            pin_num(int):使いたいピン番号
        """
        wiringpi.wiringPiSetupGpio()
        self.servo_pin = pin_num

    def move_servo(self, degree: int, sec: float) -> None:
        """Use servo.

        Args:
            degree(int):サーボを動かす角度
            sec(float):何秒待つか
        """
        sg90.sg90_set(self.servo_pin, degree)
        time.sleep(sec)

    def move_many_times_servo(self) -> None:
        """90度ずつサーボを何回も動かす(何回もメソッド呼ぶのがめんどくさいから)"""

        for i in range(14):
            sg90.sg90_set(self.servo_pin, 90)
            time.sleep(0.3)
            sg90.sg90_set(self.servo_pin, -90)
            time.sleep(0.3)


