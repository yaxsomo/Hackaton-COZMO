from machine import Pin, PWM
import time

MOTOR_DUTY_MAX = 65535
MOTOR_OFFSET_LEFT = 0
MOTOR_OFFSET_RIGHT = 0

class Motor :
    
    # Pins of each motors
    # Depending on your setup you may change the pin values
    def __init__(self, pinLeftMotorEnA, pinLeftMotorIn1, pinLeftMotorIn2, pinRightMotorEnB, pinRightMotorIn3, pinRightMotorIn4):
    
        self.motorPins={'LeftMotorEnA' : Pin(pinLeftMotorEnA, Pin.OUT),
                  "LeftMotorIn1": Pin(pinLeftMotorIn1, Pin.OUT),
                  "LeftMotorIn2": Pin(pinLeftMotorIn2, Pin.OUT),
                  "RightMotorEnB" : Pin(pinRightMotorEnB, Pin.OUT),
                  "RightMotorIn3" : Pin(pinRightMotorIn3, Pin.OUT),
                  "RightMotorIn4" : Pin(pinRightMotorIn4, Pin.OUT)}
    
    # Start motors in the chosen direction and speed
    # MotorPins are a dictionnary of Motors linked to their corresponding pins
    # SpeedRightMotor chose the speed of the angle_to_duty motors. If its negative it goes backwards, if it is positive it goes forward.
    def moveDCMotor(self, speedLeftMotor, speedRightMotor) :
        if (speedLeftMotor > MOTOR_DUTY_MAX) : 
            speedLeftMotor = MOTOR_DUTY_MAX
            
        if (speedLeftMotor < -MOTOR_DUTY_MAX) : 
            speedLeftMotor = -MOTOR_DUTY_MAX
            
        pwmEnA = PWM(self.motorPins["LeftMotorEnA"], freq=5000, duty_u16=abs(speedLeftMotor))
        pwmEnB = PWM(self.motorPins["RightMotorEnB"], freq=5000, duty_u16=abs(speedRightMotor))
        
        if (speedLeftMotor >= 0): 
            self.motorPins["LeftMotorIn1"].on()
            self.motorPins["LeftMotorIn2"].off()
        else:
            self.motorPins["LeftMotorIn1"].off()
            self.motorPins["LeftMotorIn2"].on()
        
        if (speedRightMotor >= 0): 
            self.motorPins["RightMotorIn3"].on()
            self.motorPins["RightMotorIn4"].off()
        else:
            self.motorPins["RightMotorIn3"].off()
            self.motorPins["RightMotorIn4"].on()
            
    

    def moveFastForward(self, vitesse=64535):
        self.moveDCMotor(vitesse-450, vitesse)
        
    def moveForward(self, vitesse=55535):
        self.moveDCMotor(vitesse, vitesse)
        
    def moveSlowForward(self, vitesse=45535):
        self.moveDCMotor(vitesse, vitesse)
    
    def moveFastBackward(self, vitesse=64535):
        self.moveDCMotor(-vitesse, -vitesse+450)
        
    def moveBackward(self, vitesse=55535):
        self.moveDCMotor(-vitesse, -vitesse)
    
    def moveSlowBackward(self, vitesse=45535):
        self.moveDCMotor(-vitesse, -vitesse)
        
    def turnAroundClockwise(self, vitesse=64535):
        self.moveDCMotor(vitesse, -vitesse)
    
    def turnAroundCounterClockwise(self, vitesse=64535):
        self.moveDCMotor(-vitesse, vitesse)
        
    def turnAroundClockwise90(self, vitesse=64535):
        self.moveDCMotor(vitesse, -vitesse)
        time.sleep(0.36)
        self.stop()
        
    def turnAroundCounterClockwise90(self, vitesse=64535):
        self.moveDCMotor(-vitesse, vitesse)
        time.sleep(0.45)
        self.stop()
        
    def stop(self):
        self.moveDCMotor(0, 0)

















