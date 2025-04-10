import cv2

img = cv2.imread('testPh.jpg')

img_re_linear = cv2.resize(img,None,fx=3,fy=3, interpolation=cv2.INTER_LINEAR)


img_re_cubic = cv2.resize(img,None,fx=3,fy=3,interpolation=cv2.INTER_CUBIC)


cv2.imshow('linear',img_re_linear)
cv2.imshow("cubic",img_re_cubic)
cv2.imshow('original',img)

if cv2.waitKey()==27:
    cv2.destroyAllWindows()