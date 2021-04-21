import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('C:/Users/gawta/Desktop/Abhiyaan/Section B/ComputerVision/ImageCV/abhiyaan.png')
cv2.imshow("Original", image)
kernel = np.ones((5,5),np.uint8)
kernel_ = np.ones((5,5),np.float32)/25

hist = cv2.calcHist([image], [1, 2], None, [256, 256], [30,100,150,256])
mask = cv2.calcBackProject([image], [ 1, 2], hist, [30, 100, 150, 256], 1)
new = cv2.bitwise_and(image, image, mask=mask)


cont_list, h = cv2.findContours(mask, 1, 2)
for cnt in cont_list:
    x, y, w, h = cv2.boundingRect(cnt)
    if w>3 and h>3 :
        cv2.rectangle(image,(x,y),(x+w+3,y+h+3),(255,0,0),2) 
        cv2.imshow('Gawtam', image) 

cv2.waitKey(0)
cv2.destroyAllWindows()