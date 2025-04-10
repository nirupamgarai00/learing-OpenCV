import cv2
import numpy as np

img = cv2.imread('p1.jpg')
img = cv2.resize(img,None,fx=0.3,fy=0.3)
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh_value, binary_img = cv2.threshold(grey_img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


cv2.imshow('original',img)
cv2.imshow('grey image',grey_img)
cv2.imshow('binary image',binary_img)

cv2.waitKey(0)