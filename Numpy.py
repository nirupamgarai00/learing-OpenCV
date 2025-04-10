import numpy as np

'''t = np.array([1,2,3]) # 1D array
t = np.array([(1,2,3),(5,4,6)]) # 2D array

t = np.array([[(1,2,3),(4,5,6)],[(0,9,1),(1,7,9)],[(0,9,1),(1,7,9)]]) # multidimetional array

t = np.zeros((4,4),dtype= 'bool') # to create a array of zeros with specific data type

t = np.ones((3,3),dtype='str') #to create a array of 1 with specific data type

t = np.full((3,5),3,dtype='int')#to create a array of spacific element with specific data type
t  = np.eye(3) # to get a identity matrix 3x3
t = np.arange(2,11,3) # simller to range funtion in loop
t = np.linspace(0,2,9)# 0 to 2(2 included) range and gives 9 desimal values
t= np.random.rand(2,3)# gives random values between 0 to 1
t= np.random.rand(2,3)*255# gives random values between 0 to 255
t = np.random.randint(4,size = (3,3)) ## gives random values between 0 to 3 intger valu

arr = np.array([(1,23,3),(2,3,4)])
print(arr.shape) # gives output of (row , column)
print(arr.size) # gives output as number of element 



arr = np.array([(1,23,3),(2,3,4)])

arr1 = arr.astype(float) # convert the array from int to float
print(arr1.dtype) # show the data type of the array

arr = np.array([(1,23,3),(2,3,4)])
arr1 = np.array([(1,2,3),(4,5,6)])

temp = arr+arr1 # used for adding all the element of the arrays based on index (all arthmatic oparetion +,-,*,/)
print(temp)



arr = np.array([(1,-12,23),(1,2,3)])
print(arr.max()) # gives the highest value in array
print(arr.min()) # gives the lowest value in array

   
import cv2   

img = np.full((500,500),100)

img[100:400, 100:400] = 255



cv2.imwrite('a.jpg',img)

'''
t = np.full((3,5,2),3,dtype='int')
print(t)


arr = np.zeros((2,2,2),'int')
print(arr)











