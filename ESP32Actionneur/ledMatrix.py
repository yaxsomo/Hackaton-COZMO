from machine import Pin, SPI
from max7219 import Max7219


class LedMatrix :
    
    __init__ (self, pinMosi, pinClk, pinCS, baudrateValue) :
        self.spi = SPI(baudrate=baudrateValue, polarity=1, phase=0, sck=Pin(pinClk,Pin.OUT), mosi=Pin(pinMosi,Pin.OUT))
        self.screen = Max7219(8, 8, spi, Pin(pinCS, Pin.OUT))
        
    # Display the chosen LedMatrix
    def display_ledMatrix(ledMatrix, matrix_id) :
        for i in range(8) :
            for j in range(8) :
                screen.pixel(i,j,ledMatrix[i][j])
        screen.show()
