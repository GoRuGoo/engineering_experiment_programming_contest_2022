from modules.useful_servo import UsefulServoClass

servo = UsefulServoClass(13)

servo.move_servo(90, 1.0)
servo.move_servo(-90, 0.5)
servo.move_servo(90, 1.0)
