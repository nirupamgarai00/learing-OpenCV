import cv2
import numpy as np

img = cv2.imread('testimg1.png',cv2.IMREAD_GRAYSCALE)

# normal equalization
normal_img = cv2.equalizeHist(img)


#CLAHE equalization
clahe = cv2.createCLAHE(5)
clahe_img = clahe.apply(img)


cv2.imshow('origianl',img)
cv2.imshow('normal equalization',normal_img)
cv2.imshow('clahe image',clahe_img)
cv2.waitKey(0)