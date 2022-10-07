import time

import RPi.GPIO as GPIO


class EasilyUseServoClass():
    """A class that makes working with servos easier."""

    def __init__(self, servo_pin: int):
        """Set up a servo connected to a specified pin.

        Args:
            servo_pint(_type_):Connected pin number
        Returns:
            _type_:Servo instance
        """
        GPIO.setmode(GPIO.BCM)
        self.servo_pin = servo_pin
        GPIO.setup(servo_pin, GPIO.OUT)
        instance = GPIO.PWM(servo_pin, 50)
        instance.start(0.0)
        self.instance = instance


    def rotate_to_specified_angle(self, degree: int) -> None:
        called_duty_num = int((degree * 9.5 / 180 + 2.5) * 65535 / 100)
        self.instance.ChangeDutyCycle(degree)
        time.sleep(0.5)
        GPIO.cleanup(13)

    def servo_instance_destruction(self):
        GPIO.cleanup(self.servo_pin)
