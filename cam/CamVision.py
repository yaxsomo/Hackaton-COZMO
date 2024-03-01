from cv2 import cvtColor, COLOR_BGR2HSV, countNonZero, inRange, VideoCapture, waitKey, destroyAllWindows, rectangle, COLOR_BGR2GRAY, imshow
from pyzbar.pyzbar import decode
import numpy as np
import mediapipe as mp

show = False

mp_hands = mp.solutions.hands.Hands()

def detect_color(frame):
    """
    Cette fonction détecte la couleur dominante dans une image.
    Elle utilise l'espace de couleur HSV pour détecter les couleurs.
    Elle utilise la librairie OpenCV
    
    Paramètres :
        -  frame : image RGB à traiter (ndarray)
        
    return :
        - str : couleur dominante ('bleu', 'vert', 'rouge')
    """
    
    # Convertir l'image en HSV
    hsv_frame = cvtColor(frame, COLOR_BGR2HSV)
    
    # Plages HSV pour la détection des couleurs
    lower_green = np.array([40, 50, 50])    # Plage HSV pour le vert
    upper_green = np.array([80, 255, 255])
    lower_blue = np.array([90, 50, 50])     # Plage HSV pour le bleu
    upper_blue = np.array([130, 255, 255])
    lower_red = np.array([0, 50, 50])       # Plage HSV pour le rouge
    upper_red = np.array([20, 255, 255])
    lower_white = np.array([0, 0, 180])     # Plage HSV pour le blanc
    upper_white = np.array([180, 25, 255])
    lower_gray = np.array([0, 0, 60])       # Plage HSV pour le gris
    upper_gray = np.array([180, 30, 180])
    lower_black = np.array([0, 0, 0])       # Plage HSV pour le noir
    upper_black = np.array([180, 255, 30])
    
    # Masques pour chaque couleur
    mask_green = inRange(hsv_frame, lower_green, upper_green)
    mask_blue = inRange(hsv_frame, lower_blue, upper_blue)
    mask_red = inRange(hsv_frame, lower_red, upper_red)
    mask_white = inRange(hsv_frame, lower_white, upper_white)
    mask_gray = inRange(hsv_frame, lower_gray, upper_gray)
    mask_black = inRange(hsv_frame, lower_black, upper_black)
    
    # Calculer les aires des masques
    area_green = countNonZero(mask_green)
    area_blue = countNonZero(mask_blue)
    area_red = countNonZero(mask_red)
    area_white = countNonZero(mask_white)
    area_gray = countNonZero(mask_gray)
    area_black = countNonZero(mask_black)
    
    # Déterminer la couleur dominante
    max_area = max(area_green, area_blue, area_red, area_white, area_gray, area_black)
    if max_area == area_green:
        return "Vert"
    elif max_area == area_blue:
        return "Bleu"
    elif max_area == area_red:
        return "Rouge"
    elif max_area == area_white:
        pass
    elif max_area == area_gray:
        pass
    elif max_area == area_black:
        pass
    else:
        return None
    return None


def detect_Hand(frame):
    """
    Cette fonction détecte la présence d'une main dans une image.
    Elle utilise la librairie MediaPipe.
    
    Paramètres :
        -  frame : image RGB à traiter (ndarray)
        
    return :
        - bool : True si une main est détectée, False sinon
    """
    results = mp_hands.process(frame)
    if results.multi_hand_landmarks: # multi_hand_landmarks est une liste de landmarks pour chaque main détectée
        return True
    else:
        return False
    
# Function to decode QR codes in the frame
def decode_qr(frame):
    """
    Cette fonction détecte et décode un QR code dans une image.
    Elle utilise la fonction decode de la librairie pyzbar
    
    Paramètres :
        -  frame : image RGB à traiter (ndarray)
        
    return :
        - str : données du QR code
    """
    # Convert frame to grayscale
    gray = cvtColor(frame, COLOR_BGR2GRAY)
    # Decode QR code from the frame
    decoded_objects = decode(gray)

    # If QR code is detected, draw rectangle and print data
    if decoded_objects:
        for obj in decoded_objects:
            x, y, w, h = obj.rect
            rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            qr_data = obj.data.decode('utf-8')
            return(f"QR Code Data: {qr_data}")


# Initialize the camera
cap = VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    color, qrcode, handBool = None, None, False
    #Decode the QR code or detect squares in the frame
    color = detect_color(frame)
    qrcode = decode_qr(frame)
    handBool = detect_Hand(frame)
    
    if qrcode:
        print(qrcode)
    elif handBool:
        print("Hand Detected")
    elif color:
        print(f"Couleur: {color}")
    
    # Display the resulting frame
    if show: 
        imshow('QR Code Reader', frame)
    
    
    # Exit the loop if the 'q' key is pressed
    if waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window

cap.release()
destroyAllWindows()



    