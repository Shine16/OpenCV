import cv2
import numpy as np


circles = np.zeros((4,2),np.int) # array of 4 rows , 2 height
circlesfloat = np.zeros((4,2),np.float32)
counter = 0
#print(circles)


def mousePoints(event, x, y, flags, params): # flags - if mouse clicked with shift, could give different value - detect type of click? eg left/right
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        if counter < 4 :
            circles[counter] = x, y
            circlesfloat[counter] = x, y
            counter = counter + 1
            print(circles)


img = cv2.imread('Resources/business_card.png')

'''
# by tutorial way
while True:
    if counter == 4:
        width,height = 500 , 300
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        #matrix = cv2.getPerspectiveTransform(circles,pts2)
        imgOutput = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("Warped", imgOutput)
        counter = counter+1
'''


# other way, by declaring circles as float to be compatible
while True:
    if counter == 4:
        width, height = 500, 300
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(circlesfloat,pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Warped", imgOutput)
        counter = counter + 1


    for x in range(0,4):
        cv2.circle(img,(circles[x][0], circles[x][1]), 3, (0, 0, 255), cv2.FILLED)

    cv2.imshow("Original Image",img)
    cv2.setMouseCallback("Original Image", mousePoints)
    cv2.waitKey(1)