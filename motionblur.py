#import modules
import cv2
import numpy as np



#read the img
img = cv2.imread('testPh.jpg')

#creat the kernal
kernal_15 = np.zeros((15,15),dtype=np.float32)
kernal_15[int((15-1)/2),:] = np.ones((15))
kernal_15  = kernal_15/15.0



# apply the kernal
output1 = cv2.filter2D(img,-1,kernal_15)


# show the img
cv2.imshow('original',img)
cv2.imshow('motion_blur',output1)

if cv2.waitKey() == 27:
    cv2.destroyAllWindows()