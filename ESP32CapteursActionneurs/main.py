from machine import Pin, PWM, SPI
import time
from max7219 import Max7219
from LedMatrixConst import *
from ledMatrix import *
from motor import *
from servoMotor import *


# # # SET DEFAULT BEHAVIOUR # # #
ledBoard = LedMatrix(pinMosi=23, pinClk=18, pinCS=5, baudrateValue=10000000)
motor = Motor(27, 26, 25, 14, 33, 32)
servo = ServoMotor(21)

#time.sleep(2.5)
#ledBoard.display_ledMatrix(ledMatrix_dollar)
#ledBoard.testone()
#time.sleep(5)
#servo.defaultPos()

servo.moveServo(90)
#print(servo.current_angle)

# servo.defaultPos()
# servo.moveServo(150)

time.sleep(4)
ledBoard.display_ledMatrix(ledMatrix_neutral)
motor.moveFastForward()
time.sleep(2)
motor.turnAroundClockwise90()
time.sleep(0.5)
motor.turnAroundClockwise90()
time.sleep(0.5)
motor.turnAroundClockwise90()
time.sleep(0.5)
motor.turnAroundClockwise90()
time.sleep(0.5)
motor.moveFastBackward()
time.sleep(2)
motor.turnAroundCounterClockwise()
time.sleep(2.5)
motor.stop()
ledBoard.display_ledMatrix(ledMatrix_spiral)
time.sleep(1.5)
ledBoard.display_ledMatrix(ledMatrix_eye_closed)
time.sleep(1)
ledBoard.display_ledMatrix(ledMatrix_heart)
#servo.moveServo(90)
time.sleep(1.5)
ledBoard.display_ledMatrix(ledMatrix_dollar)


"""
Avant
360
Arrière
Spin
Spiral
Heart
Effort + Arm push
Money
Arm dance
"""


# # # INFRAROUGE # # #
# infrarouge = Pin(4, Pin.IN)
# while True : 
#   valueInfrarouge = infrarouge.value()
#   print(valueInfrarouge)
#   time.sleep(2)









































