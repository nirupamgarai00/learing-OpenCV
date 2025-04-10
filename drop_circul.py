import cv2
import numpy as np
img = np.zeros((500,500,3),np.uint8) 
def draw_circul(evant,x,y,flag,pram):
    if(evant == cv2.EVENT_LBUTTONDBLCLK):
        cv2.circle(img,(x,y),5,(255,255,255),2)


# this functtion is use to name a window
cv2.namedWindow('window')

cv2.setMouseCallback('window',draw_circul) # tracs the coordinates of the mouse and based on that call the draw_circul function

# used to show the window in 60 FPS
while(1):
    cv2.imshow('window',img)
    if cv2.waitKey(17) == 27:
        break
cv2.destroyAllWindows()