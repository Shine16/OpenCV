import cv2
import numpy as np

img = cv2.imread('Resources/business_card.png')


# got points from image in paint, open and scroll mouse to corner
pts1 = np.float32([[34, 91],[408 , 11],[131,335],[539, 194]])
print(pts1)
# 1 ----- 2
# |       |
# |       |
# |       |
# 3 ----- 4


width,height = 500 , 300 # approximately
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# two functions for warping
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

# draw circles at points to show got the points right
for x in range(0,4):
    cv2.circle(img,(pts1[x][0],pts1[x][1]),5,(0,0,255),cv2.FILLED)

cv2.imshow("Original",img)
cv2.imshow("Warped",imgOutput)

cv2.waitKey(0)