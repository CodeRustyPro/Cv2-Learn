import cv2
import numpy

img = cv2.imread('resources/image2.jpg')
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("1",img)
cv2.imshow("2",imgHSV)
cv2.waitKey(0)