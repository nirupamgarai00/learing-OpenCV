import cv2
import numpy as np

img = cv2.imread('testPh.jpg')

matrix = np.float32([[1,0,100],[0,1,100]]) # for translation

translated = cv2.warpAffine(img,matrix,(img.shape[0]+100,img.shape[1]+100))

cv2.imshow('org',img)
cv2.imshow('translated',translated)

if (cv2.waitKey()==27):
    cv2.destroyAllWindows()