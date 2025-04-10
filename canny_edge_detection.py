#import modeles
import cv2
import numpy as np

img = cv2.imread('img.jpg')
lower = 0
upper = 0

def show(lower,upper):
    global img
    output = cv2.Canny(img,lower,upper)
    cv2.imshow('track',output)
    cv2.waitKey(0)

def onchange(value):
    global lower,upper
    lower = 25*value
    upper = 50*value
    show(lower,upper) 
    
    
    


cv2.namedWindow('track')
cv2.createTrackbar('change_lower','track',1,10,onchange)

