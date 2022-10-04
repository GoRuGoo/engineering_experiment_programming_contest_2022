import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

gp_out = 13
GPIO.setup(gp_out, GPIO.OUT)
right = GPIO.PWM(gp_out, 50)
right.start(0.0)

gp_out = 18
GPIO.setup(gp_out, GPIO.OUT)
left = GPIO.PWM(gp_out, 50)
left.start(0.0)


bot = 2.5
mid = 7.2
top = 12.0

right.ChangeDutyCycle(bot)
left.ChangeDutyCycle(bot)
time.sleep(0.5)


right.ChangeDutyCycle(top)
time.sleep(0.5)

right.ChangeDutyCycle(bot)
left.ChangeDutyCycle(top)
time.sleep(0.5)

right.ChangeDutyCycle(top)
left.ChangeDutyCycle(bot)
time.sleep(0.5)

GPIO.cleanup()
