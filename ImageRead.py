import cv2
import numpy


img = cv2.imread("Resources/lena.png") # read lena png image
cv2.imshow("Lena",img) # window to show image


cv2.waitKey(0)  # wait for infinite