import cv2 
import numpy as np

img = cv2.imread("resources/image2.jpg")
colorImg = np.zeros((1920,1080,3))
kernel = np.ones((5,5),np.uint8)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(7,7),0)
imgCanny = cv2.Canny(img,100,200,1)
imgDialated = cv2.dilate(imgCanny,kernel,iterations=2)

cv2.putText(img,"Dev Shah",(100,100),cv2.FONT_HERSHEY_PLAIN,4,(255,0,0),1)
cv2.imshow('Colorimg',colorImg)
cv2.imshow("Original",img)
cv2.imshow("1234",imgGray)
cv2.imshow("12345",imgBlur)
cv2.imshow("123456",imgCanny)
cv2.imshow("1234356",imgDialated)

cv2.waitKey(0)
print(img)