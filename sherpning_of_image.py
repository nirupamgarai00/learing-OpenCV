import cv2
import numpy as np

img = cv2.imread('img.jpg')

# to sherpning a image we need to subtract the blur version that image
# lets use guassian blur
gaussian_blur = cv2.GaussianBlur(img,(11,11),2)


# sheroning of image - we use addweited function
sherped1 = cv2.addWeighted(img,7.5,gaussian_blur,-6.5,0)


cv2.imshow('original',img)
cv2.imshow('sherped',sherped1)

cv2.waitKey(0)