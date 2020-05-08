import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)
# all ones, matric 5 by 5, unsigned 8 bits 0-255

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html

imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
#image, kernal size (has to be odd number), sigma
#https://en.wikipedia.org/wiki/Gaussian_blur

imgCanny = cv2.Canny(img,150,200)
# image, threshold, threshold
# to find edges

imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# numpy deal with matrices
# thicker lines https://docs.opencv.org/2.4/doc/tutorials/imgproc/erosion_dilatation/erosion_dilatation.html

imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
# thinner lines - dilate and erode

cv2.imshow("Gray Image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)
