from machine import Pin, PWM

class ServoMotor :
    
    def _init_(self, servoPin) :
        self.servoPin = Pin(servoPin, Pin.OUT)
    
    # Transform an angle to a PWM duty exploitable for the SG90
    def angle_to_duty(angle):
        min_duty = 26
        max_duty = 128
        return int(min_duty + (angle / 180.0) * (max_duty - min_duty))
    
    # Move the selected Servo-Motor
    
    def moveServo(self, angle)  :
        PWM(servoPin, freq=50, duty=angle_to_duty(angle))
