import cv2
import numpy as np

# for getting fram from camera
def get_fram(cap):
    ret ,fram = cap.read()
    fram = cv2.resize(fram,None,fx=0.4,fy=0.4,interpolation=cv2.INTER_CUBIC)
    fram = cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
    return cv2.GaussianBlur(fram,(5,5),0)

# to calculate fram differnce
def fram_defference(p_fram,c_fram,n_fram):
    diff1 = cv2.absdiff(p_fram,c_fram)
    diff2 = cv2.absdiff(c_fram,n_fram)
    result = cv2.bitwise_and(diff1,diff2)
    
    return result
    

# taking input from camera
cap = cv2.VideoCapture(0)

# geting frams
p_fram = get_fram(cap)
c_fram = get_fram(cap)
n_fram = get_fram(cap)

while True:
    
    # storing the fram diffrence result
    diff_fram = fram_defference(p_fram,c_fram,n_fram)
    
    # do use it it is for visuals only
    _,threshold = cv2.threshold(diff_fram,0,255,cv2.THRESH_TRIANGLE)
    
    cv2.imshow('original',diff_fram)
    cv2.imshow('envanced',threshold)
    
    p_fram = c_fram
    c_fram = n_fram
    n_fram = get_fram(cap)
    
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows
    