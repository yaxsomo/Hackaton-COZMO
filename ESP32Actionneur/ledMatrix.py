from machine import Pin, PWM, SPI




class LedMatrix :
    
    __init__ (self, pinMosi, pinClk 
    # Display the chosen LedMatrix
    def display_ledMatrix(ledMatrix, matrix_id) :
        for i in range(8) :
            for j in range(8) :
                screen.pixel(i,j,ledMatrix[i][j])
        screen.show()
