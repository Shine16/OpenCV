# warp prospective

import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# numpy array of 4 different points to extract warped image
# can use paint to see value of pixels

pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# need to define which corner is origin - still dont really understand

matrix = cv2.getPerspectiveTransform(pts1,pts2)
# get transformation matrix

imgOutput = cv2.warpPerspective(img,matrix,(width,height))
# image output 


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)
