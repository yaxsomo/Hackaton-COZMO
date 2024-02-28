from machine import Pin, PWM, SPI
import time
from max7219 import Max7219
# def degre_to_1024(degre):
#     print((1024/180) * degre)
#     return int((1024/180) * degre)
def display_ledMatrix(ledMatrix) :
    for i in range(8) :
        for j in range(8) :
            screen.pixel(i,j,ledMatrix[i][j])
    screen.show()

spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(18), mosi=Pin(23))
ss = Pin(5, Pin.OUT)
screen = Max7219(8, 8, spi, Pin(5))
screen.pixel(0,0,1)
screen.show()

ledMatrix_enerve= [ [0, 0, 0, 1, 0,0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 1, 0, 1, 1, 1, 0, 0],
                     [0, 0, 1, 1, 1, 1, 1, 0],
                     [0, 0, 1, 1, 0, 1, 1, 0],
                     [0, 0, 1, 1, 1, 1, 1, 0],
                     [0, 0, 0, 1, 1, 1, 0, 0]]



ledMatrix_dollar = [ [0, 0, 0, 1, 0,0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 0, 0, 0, 0],
                     [1, 0, 1, 1, 1, 0, 0, 0],
                     [0, 1, 1, 1, 1, 1, 0, 0],
                     [0, 1, 1, 0, 1, 1, 0, 0],
                     [0, 1, 1, 1, 1, 1, 0, 0],
                     [0, 0, 1, 1, 1, 0, 0, 0]]

display_ledMatrix(ledMatrix_enerve)





# display.text('4',0,0,1)
# display.show()    

# def angle_to_duty(angle):
#     min_duty = 26
#     max_duty = 128
#     return int(min_duty + (angle / 180.0) * (max_duty - min_duty))

# ena = Pin(27, Pin.OUT)
# in1 = Pin(26, Pin.OUT)
# in2 = Pin(25, Pin.OUT)
# in1.on()
# in2.off()
# 
# enb = Pin(14, Pin.OUT)
# in3 = Pin(33, Pin.OUT)
# in4 = Pin(32, Pin.OUT)
# in4.off()
# in3.on()

#chauve
# servo1 = Pin(21, Pin.OUT)
# pwmservo1 = PWM(servo1, freq=50, duty=angle_to_duty(0))
# 
# servo2 = Pin(22, Pin.OUT)
# pwmservo2 = PWM(servo2, freq=50, duty=angle_to_duty(180))

# #vert
# pwm1 = PWM(ena, freq=5000, duty_u16=41768)
# 
# pwm2 = PWM(enb, freq=5000, duty_u16=45768)

# while True :
#     time.sleep(2)
#     print(in3.value())
#     print(in4.value())

# infrarouge = Pin(4, Pin.IN)
# while True : 
#   valueInfrarouge = infrarouge.value()
#   print(valueInfrarouge)
#   time.sleep(2)








































