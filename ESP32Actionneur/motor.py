from machine import Pin, PWM

MOTOR_DUTY_MAX = 65535
MOTOR_OFFSET_LEFT = 0
MOTOR_OFFSET_RIGHT = 0

class Motor :
    
    # Pins of each motors
    # Depending on your setup you may change the pin values
    def __init__(self, pinLeftMotorEnA, pinLeftMotorIn1, pinRightMotorEnB, pinRightMotorIn3, pinRightMotorIn4)
    
        self.motorPins{"LeftMotorEnA": Pin(pinLeftMotorEnA, Pin.OUT),
                  "LeftMotorIn1": Pin(pinLeftMotorIn1, Pin.OUT),
                  "LeftMotorIn2": Pin(pinLeftMotorIn2, Pin.OUT),
                  "RightMotorEnB" : Pin(pinRightMotorEnB, Pin.OUT),
                  "RightMotorIn3" : Pin(pinRightMotorIn3, Pin.OUT),
                  "RightMotorIn4" : Pin(pinRightMotorIn4, Pin.OUT)}
    
    # Start motors in the chosen direction and speed
    # MotorPins are a dictionnary of Motors linked to their corresponding pins
    # SpeedRightMotor chose the speed of theangle_to_duty motors. If its negative it goes backwards, if it is positive it goes forward.
    def moveDCMotor(self, speedLeftMotor, speedRightMotor) :
        if (speedLeftMotor > MOTOR_DUTY_MAX) : 
            speedLeftMotor = MOTOR_DUTY_MAX
            
        if (speedLeftMotor < -MOTOR_DUTY_MAX) : 
            speedLeftMotor = -MOTOR_DUTY_MAX
            
        pwmEnA = PWM(self.motorPins["LeftMotorEnA"], freq=5000, duty_u16(abs(speedLeftMotor)))
        pwmEnB = PWM(self.motorPins["RightMotorEnB"], freq=5000, duty_u16(abs(speedRightMotor)))
        
        if (speedLeftMotor >= 0) : 
            self.motorPins["LeftMotorIn1"].on()"RightMotorIn3"
            self.motorPins["LeftMotorIn2"].off()
        else 
            self.motorPins["LeftMotorIn1"].off()
            self.motorPins["LeftMotorIn2"].on()
        
        if (speedRightMotor >= 0) : 
            self.motorPins["RightMotorIn3"].off()
            self.motorPins["RightMotorIn4"].on()
        else 
            self.motorPins["RightMotorIn3"].on()
            self.motorPins["RightMotorIn4"].off()
