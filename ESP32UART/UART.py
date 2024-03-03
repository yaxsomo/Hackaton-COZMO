from machine import UART



class Link :
    
    def __init__(self):
        self.uart1 = UART(1, baudrate=9600, tx=33, rx=32)
    
    def uartReadAllBytes(self) :
       uart1.read()  
    
    def uartReadNbBytes(self,nbBytesToRead) :
       uart1.read(nbBytesToRead)    

    def uartWrite(self,message) :
        uart.write(message)
