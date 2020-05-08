import cv2
import numpy as np

img = cv2.imread("Resources/shapes.png")
print(img.shape) # prints image pixels, height, width, number of channels (BGR)
#(577, 576, 3)

imgResize = cv2.resize(img,(1000,500))
print(imgResize.shape)
#(500, 1000, 3)

imgCropped = img[46:119,352:495] # height:height , width:width
# image is an array of pixels



cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCropped)

cv2.waitKey(0)



