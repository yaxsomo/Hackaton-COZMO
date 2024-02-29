from machine import Pin, PWM
import time

class ServoMotor :
    
    def __init__(self, servoPin) :
        self.servoPin = Pin(servoPin, Pin.OUT)
        self.current_angle = 90
        self.default_angle = 90
        
        #self.defaultPos()
    
    # Transform an angle to a PWM duty exploitable for the SG90
    def angle_to_duty(self, angle):
        min_duty = 26
        max_duty = 128
        return int(min_duty + (angle / 180.0) * (max_duty - min_duty))
    
    # Move the selected Servo-Motor
    def moveServo(self, angle)  :
        #PWM(self.servoPin, freq=50, duty=self.angle_to_duty(angle))
        if angle > self.current_angle:
            for i in range (angle - self.current_angle):
                PWM(self.servoPin, freq=50, duty=self.angle_to_duty(self.current_angle + i))
                time.sleep(0.01)
        elif angle < self.current_angle:
            for i in range (self.current_angle - angle):
                PWM(self.servoPin, freq=50, duty=self.angle_to_duty(self.current_angle - i))
                time.sleep(0.01)
        else:
            return
        self.current_angle = angle
        
    def defaultPos(self):
        self.moveServo(self.default_angle)
        self.current_angle = self.default_angle
        









