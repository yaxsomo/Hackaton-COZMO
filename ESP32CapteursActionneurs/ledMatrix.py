from machine import Pin, PWM, SPI
from max7219 import Max7219
from LedMatrixConst import *
import time


class LedMatrix :
    
    def __init__ (self, pinMosi, pinClk, pinCS, baudrateValue):
        self.spi = SPI(1, baudrate=baudrateValue, polarity=1, phase=0, sck=Pin(pinClk), mosi=Pin(pinMosi))
        self.ss = Pin(pinCS, Pin.OUT)
        self.screen = Max7219(8, 8, self.spi, self.ss)
        
    def default_eyes(self):
        self.display_ledMatrix(ledMatrix_neutral)
        
        
    # Display the chosen LedMatrix
    def display_ledMatrix(self, ledMatrix) :
        for i in range(8) :
            for j in range(8) :
                self.screen.pixel(i,j,ledMatrix[i][j])
        self.screen.show()
        
    def testone(self):
#         self.screen.pixel(0,6,1)
#         self.screen.pixel(1,7,1)
#         self.screen.pixel(2,7,1)
#         self.screen.pixel(3,7,1)
#         self.screen.pixel(4,7,1)
#         self.screen.pixel(5,7,1)
#         self.screen.pixel(6,7,1)
#         self.screen.pixel(7,7,1)
        self.screen.fill(1)
        self.screen.show()
