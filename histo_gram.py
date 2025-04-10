import cv2
import numpy as np
from matplotlib import pyplot as plt # used to plot histogram

img = cv2.imread('test1.png')# read the image into matrix from

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#used convert colerspace

hist = cv2.calcHist([img],[0],None,[256],[0,255])# for calculating historgram

img_hist = cv2.equalizeHist(img) #for histogram equalization

equlized_hist = cv2.calcHist([img_hist],[0],None,[256],[0,255]) # histogram of equalized image
plt.plot(equlized_hist)# used to plot the histogram into graph format

plt.plot(hist)


cv2.imshow('original',img)
cv2.imshow('equalized image',img_hist)

plt.show() # used to show the ploted histogram
cv2.waitKey(0)
