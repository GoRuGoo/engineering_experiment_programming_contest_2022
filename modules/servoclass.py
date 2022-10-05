import time

import RPi.GPIO as GPIO


class EasilyUseServoClass:
    """A class that makes working with servos easier."""

    def __init__(self, servo_pin: int):
        """Set up a servo connected to a specified pin.

        Args:
            servo_pint(_type_):Connected pin number
        Returns:
            _type_:Servo instance
        """
        self.servo_pin = servo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servo_pin, 50)
        servo_instance = GPIO.PWM(servo_pin, 50)
        servo_instance.start(0.0)
        self.servo_instance = servo_instance

    def rotate_to_specified_angle(self, degree: int) -> None:
        called_duty_num = int((degree * 9.5 / 180 + 2.5) * 65535 / 100)
        self.servo_instance.ChangeDutyCycle(called_duty_num)
        time.sleep(1.0)

    def servo_instance_destruction():
        GPIO.cleanup()
