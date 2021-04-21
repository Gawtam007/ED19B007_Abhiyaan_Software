import cv2 as cv
import imutils 
   
#Histogram of Oriented Gradients
hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())
   
vid = cv.VideoCapture('C:/Users/gawta/Desktop/Abhiyaan/Section B/ComputerVision/VideoCV/pedestrians.mp4')
   
while vid.isOpened():

    ret, frame = vid.read() # reads video framewise
    if ret:
        frame = imutils.resize(frame, width=min(400, frame.shape[1]))

        (regions, _) = hog.detectMultiScale(frame, winStride=(4, 4), padding=(4, 4), scale=1.2)   
        for (x, y, w, h) in regions:
            cv.rectangle(frame, (x, y) , (x + w, y + h) , (0, 0, 255) , 2 )
   
        cv.imshow("frame", frame)

        #press enter to exit
        if cv.waitKey(33) == 13:
            break
    else:
        break
  
vid.release()
cv.destroyAllWindows()

#reference : 
# 1. https://www.youtube.com/watch?v=oXlwWbU8l2o
# 2. https://morioh.com/p/104c69d549dd
# 3. https://www.geeksforgeeks.org/pedestrian-detection-using-opencv-python/