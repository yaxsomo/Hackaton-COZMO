import time
from machine import UART
import uos

# Initialize UART for serial communication
uart = UART(1, baudrate=9600, tx=17, rx=16)

# Define constants for frame size
FRAME_WIDTH = 120
FRAME_HEIGHT = 90
CHUNK_SIZE = 2048  # Adjust as needed

# Main loop
while True: 
    try:
        # Take a snapshot and store it in RAM
        uart.write("Taking snapshot...\n")
        
        # Capture a frame and send it in chunks
        for chunk_start in range(0, FRAME_WIDTH * FRAME_HEIGHT * 2, CHUNK_SIZE):
            chunk_end = min(chunk_start + CHUNK_SIZE, FRAME_WIDTH * FRAME_HEIGHT * 2)
            frame_chunk = bytearray(CHUNK_SIZE)
            
            # Capture a chunk of the frame and store it in the buffer
            uos.dupterm_notify(True)
            time.sleep(0.1)  # Allow some time for the frame to be captured
            uos.dupterm_notify(False)
            
            # Send the chunk bytes over serial
            uart.write(frame_chunk)
        
        # Wait for a short time before capturing the next frame
        time.sleep(2)
        
    except Exception as e:
        print("Error:", e)

