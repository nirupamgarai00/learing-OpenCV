import cv2
import numpy as np

img = cv2.imread('img.jpg')

# sobel edge detection
sobal_x = cv2.Sobel(img,-1,1,0)
sobal_y = cv2.Sobel(img,-1,0,1)
sobel_edge = cv2.addWeighted(sobal_x,0.5,sobal_y,0.5,0)

# scherr edge dection
scharr_x = cv2.Scharr(img,-1,0,1)
scharr_y = cv2.Scharr(img,-1,1,0)
scharr_image = cv2.addWeighted(scharr_x,0.5,scharr_y,0.5,0)

# laplation edge detection
laplacian_image = cv2.Laplacian(img,-1,ksize=7)


cv2.imshow('sobel edged image',sobel_edge)
cv2.imshow('scharr edge detection image',scharr_image)
cv2.imshow('laplecian edge detection image',laplacian_image)
cv2.waitKey(0)
