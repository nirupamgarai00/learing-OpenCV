import  cv2

img = cv2.imread('testPh.jpg')

h= img.shape[0]
w = img.shape[1]

matrix = cv2.getRotationMatrix2D((h/2,w/2),15,1) #  this module is used to genereate the rotation matrix

translated = cv2.warpAffine(img,matrix,(h,w))# this module is used to apply the matrix

cv2.imshow('roation',translated)

if cv2.waitKey()==27:
    cv2.destroyAllWindows()