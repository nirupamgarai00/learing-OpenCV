import cv2
import numpy as np

canvas = np.full((1000,1000,3),255,dtype=np.uint8) # creat a 3D array 1000x1000 and 3 is for RGB color

# defin a line 
cv2.line(canvas,(0,0),(100,100),(255,0,0),3,cv2.LINE_4) # with LINE_4 line type
cv2.line(canvas,(105,105),(200,200),(255,0,0),3,cv2.LINE_AA) # with LINE_AA type

# drawing a rectengle
cv2.rectangle(canvas,(500,500),(700,700),(0,255,0),-1,cv2.LINE_4)

# drawing a circle
cv2.circle(canvas,(250,250),20,(0,0,0),-1)

# drwaing a arrowed line
cv2.arrowedLine(canvas,(600,10),(600,100),(0,0,0),tipLength=0.2)

# drawing a polygon


#Making a empty BLACK canvas
#Here canvas is of three layers
canvas = np.zeros((300,300,3))

#Required points we need to join
pts = np.array([[250, 5], [220, 80], [280, 80],[100,100],[250,250]], np.int32)

# Reshape the points to shape (number_vertex, 1, 2)
pts = pts.reshape((-1, 1, 2))# -1 tella openCV to automaticaly calculate the number for vertex, 1 -> Adds a dimension, so each vertex becomes its own "group.", 2 -> last dimension of the x and y coordinate

# Draw this polygon 
#Here Boolean True and Flase determine if the figure is closed
cv2.polylines(canvas, [pts], True,(0,255,0),3)





cv2.imshow('test1',canvas)
cv2.waitKey()
cv2.destroyAllWindows()



