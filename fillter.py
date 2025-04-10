# import module
import cv2
import numpy as np

# imort the the img
img = cv2.imread('testPh.jpg')

# create kerlan matrix
kernal_3 = np.ones((3,3),dtype= np.float32)/9.0
kernal_11 = np.ones((11,11),dtype=np.float32)/121.0



# apply to the img

output_1 = cv2.filter2D(img,-1,kernal_3)
output_2 = cv2.filter2D(img,-1,kernal_11)


# show the image
cv2.imshow('original',img)
cv2.imshow('blur_3',output_1)
cv2.imshow('blur_11',output_2)

if cv2.waitKey() == 27:
    cv2.destroyAllWindows()
