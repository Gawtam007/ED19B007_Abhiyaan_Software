import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# blank = np.zeros((500,500),dtype = 'uint8')
# cv.imshow('Blank',blank) 

img = cv.imread('C:/Users/gawta/Desktop/Abhiyaan/Section B/ComputerVision/ImageCV/abhiyaan.png')
hsv_orginal = cv.cvtColor(img, cv.COLOR_BGR2HSV)

grass = cv.imread("C:/Users/gawta/Desktop/Abhiyaan/Section B/ComputerVision/ImageCV/neg.jpg")
hsv_grass = cv.cvtColor(grass, cv.COLOR_BGR2HSV)

#hue, saturation, value = cv.split(hsv_grass)

grass_hist = cv.calcHist([hsv_grass], [0,1], None, [180, 256], [0, 180, 0, 256])
mask = cv.calcBackProject([hsv_orginal], [0, 1], grass_hist, [0, 180, 0, 256], 1)

# Filtering remove noise
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
mask = cv.filter2D(mask, -1, kernel)
_, mask = cv.threshold(mask, 100, 255, cv.THRESH_BINARY)

mask = cv.merge((mask, mask, mask))
result = cv.bitwise_and(img, mask)

cv.imshow("Mask", mask)
cv.imshow("Original image", img)
cv.imshow("Result", result)
cv.imshow("Grass", grass)


cv.waitKey(0)
cv.destroyAllWindows()