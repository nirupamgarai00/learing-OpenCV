import cv2
'''                            #USED TO CHANGE THE COLOR OF THE IMAGE
img = cv2.imread("test.png", cv2.IMREAD_GRAYSCALE)       #  <-  reading a image

# function to print a image
cv2.imshow('testcase',img) # show the img in a window
cv2.waitKey() # show window from a certain time (untill any key pressed)

# funtion to show a video 

cap = cv2.VideoCapture(0) # instance of the videoCapture class
opened = cap.isOpened() # checks camera is opened or Not and stored it

if(opened): # cheking for True 
    while(cap.isOpened()): # looping the video
        ret, fram = cap.read() # ret is fram is available fram is simple video fram 
        
        if(ret == True): # checks the  fram us avalable ??
            cv2.imshow('test',fram) # show the fram
            
            if (cv2.waitKey(1)==27): # show the fram untill 'Esc' key in keyboard got pressed
            break

cap.release() # release the memmory 
cv2.destroyAllWindows() # destroy all windows
            
'''        



# funtion to capture a video and stored in memory

cap = cv2.VideoCapture(0) # instance of the videoCapture class
opened = cap.isOpened() # checks camera is opened or Not and stored it
fourcc = cv2.VideoWriter_fourcc(*'MJPG')



H = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
W = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
FPS = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('test.avi',fourcc,30.0,(int(W),int(H)))
if(opened): # cheking for True 
    while(cap.isOpened()): # looping the video
        ret, frame = cap.read() # ret is fram is available fram is simple video fram 
        
        if(ret == True): # checks the  fram us avalable ??
            cv2.imshow('test',frame) # show the fram
            out.write(frame)
            
            if (cv2.waitKey(1)==27): # show the fram untill 'Esc' key in keyboard got pressed
             break

cap.release() # release the memmory 
out.release() # release the memmory
cv2.destroyAllWindows() # destroy all windows
            


