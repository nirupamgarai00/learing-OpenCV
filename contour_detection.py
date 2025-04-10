import cv2
import numpy as np

img = cv2.imread('p2.jpg')
img = cv2.resize(img,None,fx=0.4,fy=0.4)

g_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
g_img = cv2.GaussianBlur(g_img,(5,5),0)
thresh_value,b_img = cv2.threshold(g_img,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# gives a list contours
contour,hierachy = cv2.findContours(b_img,mode=cv2.RETR_TREE,method=cv2.CHAIN_APPROX_NONE)

print('len of contour = {}'.format(len(contour)))
#print(contour)

copy_img = img.copy()

# used to draw contours
copy_img = cv2.drawContours(copy_img,contour,-1,(255,0,255),2)

cv2.imshow('original',img)
cv2.imshow('binary',b_img)
cv2.imshow('contour image',copy_img)

cv2.waitKey(0)