# Import the module
import cv2
import numpy as np

def set(value):
    pass  # Placeholder function for trackbars

# Create a window and trackbars
cv2.namedWindow('adjust object')
cv2.createTrackbar('uper_hue', "adjust object", 255, 255, set)
cv2.createTrackbar('uper_brightnes', "adjust object", 255, 255, set)
cv2.createTrackbar('uper_saturation', "adjust object", 255, 255, set)
cv2.createTrackbar('lower_hue', "adjust object", 0, 255, set)
cv2.createTrackbar('lower_brightnes', "adjust object", 0, 255, set)
cv2.createTrackbar('lower_saturation', "adjust object", 0, 255, set)

def get_fram(cap, scaling_factor):
    ret, fram = cap.read()  # Unpack the tuple returned by cap.read()
    
    # Resize the frame if scaling_factor is provided
    if scaling_factor:
        fram = cv2.resize(fram, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    return fram

cap = cv2.VideoCapture(0)
while True:
    fram = get_fram(cap, None)
    

    hsv = cv2.cvtColor(fram, cv2.COLOR_BGR2HSV)

    # Get trackbar positions
    u_hue = cv2.getTrackbarPos('uper_hue', 'adjust object')
    u_brightes = cv2.getTrackbarPos('uper_brightnes', 'adjust object')
    u_saturation = cv2.getTrackbarPos('uper_saturation', 'adjust object')
    l_hue = cv2.getTrackbarPos('lower_hue', 'adjust object')
    l_brightnes = cv2.getTrackbarPos('lower_brightnes', 'adjust object')
    l_saturation = cv2.getTrackbarPos('lower_saturation', 'adjust object')

    # Define upper and lower bounds as lists
    uper = [u_hue, u_saturation, u_brightes]
    lower = [l_hue, l_saturation, l_brightnes]

    # Create a mask and apply it
    mask = cv2.inRange(hsv, np.array(lower), np.array(uper))
    res = cv2.bitwise_and(fram, fram, mask=mask)
    res = cv2.medianBlur(res, 5)

    # Display the original and detected frames
    cv2.imshow('original', fram)
    cv2.imshow('detected', res)

    # Exit on pressing 'Esc'
    if cv2.waitKey(7) == 27:
        break

cap.release()
cv2.destroyAllWindows()