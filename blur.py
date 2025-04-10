import cv2
import numpy as np

img = cv2.imread('testPh.jpg')
img2 = cv2.imread('img.jpg')

# kernal bluring with fillter2D
Kernal = np.ones((25,25),dtype=np.float32) /625.0

output1 = cv2.filter2D(img,-1,Kernal)

# blur function
output2 = cv2.blur(img,(25,25))

# boxfillter funtion
output3 = cv2.boxFilter(img,-1,(3,3),normalize=False)

# gausion blur
output4 = cv2.GaussianBlur(img,(25,25),0)

# meadiun blur
output5 = cv2.medianBlur(img,25)

# belatral fillering (reduction image + presaved edges)

output6 = cv2.bilateralFilter(img2,200,1,1)



cv2.imshow('kernal blur',output1)
cv2.imshow('blur funtion',output2)
cv2.imshow('boxfillter function',output3)
cv2.imshow('gaussian Blur',output4)
cv2.imshow('median blur',output5)
cv2.imshow('belatral fillering',output6)

cv2.imshow('original',img2)


if cv2.waitKey() == 27:
    cv2.destroyAllWindows()





