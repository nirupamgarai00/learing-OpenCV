import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test1.png')

bgr2hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(bgr2hsv_img)

v = cv2.equalizeHist(v)

hist = cv2.calcHist([v],[0],None,[256],[0,255])
plt.plot(hist)
hist = cv2.calcHist([s],[0],None,[256],[0,255])
plt.plot(hist)
hist = cv2.calcHist([h],[0],None,[256],[0,255]) 
plt.plot(hist)
bgr2hsv_img = cv2.merge([h,s,v])    

img_hsv2bgr = cv2.cvtColor(bgr2hsv_img,cv2.COLOR_HSV2BGR)



cv2.imshow('original',img)
cv2.imshow('equaliezd image',img_hsv2bgr)
plt.show()
cv2.waitKey(0)
