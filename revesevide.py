
# sudo pip install opencv-python
import cv2 # import the cv2 moduel
  
    


cap = cv2.VideoCapture('test.avi') #instance of the class
opened =  cap.isOpened() # checks cv2 in capable of opening this file

f_count = cap.get(cv2.CAP_PROP_FRAME_COUNT) # count the number of frames in the video

h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # height of the frame
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # width of the frame 
fps = cap.get(cv2.CAP_PROP_FPS) # fps of the video

f_index = f_count-1 # last index of the frames

fourcc = cv2.VideoWriter_fourcc(*'MJPG') # define a codec

out = cv2.VideoWriter('revered1.avi',fourcc, fps,(int(w),int(h))) # instane of the video writer class


if opened: # checks if True
    while (f_index != 0): 
        cap.set(cv2.CAP_PROP_POS_FRAMES,f_index) # setting the video to a sepesific frame_index
        
        ret , frame = cap.read() # read the frame
        
        out.write(frame) # writting the frame
        
        f_index -=1 # itteration
        
        # checking the progress
        if f_index%100 == 0: 
            print(f_index)
  
# releasing memory      
out.release()
cap.release()

cv2.destroyAllWindows()# destroying the window
        
        


        
        



