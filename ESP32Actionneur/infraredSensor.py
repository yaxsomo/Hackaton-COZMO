from machine import Pin


class InfraredSensor :
    
    __init__ (self, pinInfrared) :
        self.infrared = Pin(pinInfrared,Pin.IN)
        
    # Return infrared Value
    def getInfraredValue() :
        return infrared.value()
