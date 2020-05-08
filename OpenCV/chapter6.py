# useful when have alot of images

import cv2
import numpy as np


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)# https://www.w3schools.com/python/ref_func_isinstance.asp , return true if imArray is instance of list
    width = imgArray[0][0].shape[1] #https://www.w3schools.com/python/numpy_array_shape.asp , returns array dimensions, no of elements in each dimension
    height = imgArray[0][0].shape[0]
    
    if rowsAvailable: # has height and width, rows and columns
        
        for x in range ( 0, rows): # resizes the images to be standard?
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR) # makes picture 2 a grayscale
                    
        imageBlank = np.zeros((height, width, 3), np.uint8) # generate black image of height and width, BGR
        hor = [imageBlank]*rows # array of numpy arrays
        #http://scipy-lectures.org/intro/numpy/operations.html
        hor_con = [imageBlank]*rows # not used
        
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x]) # stack rows 
            
        ver = np.vstack(hor) # imArray is 3 x 2 , stacks the columns
        
    else: # has only rows , no columns
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]: # think this checks and resizes images to be equal
                # https://numpy.org/devdocs/reference/generated/numpy.shape.html
                # https://www.reddit.com/r/scipy/comments/4zdh9x/what_does_numpys_imageshape2_do/
                # https://stackoverflow.com/questions/8556076/python-how-to-extract-the-last-x-elements-from-a-list/8556080 [:2] is first 2 elements
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)# https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR) # makes picture 2 a grayscale
        hor= np.hstack(imgArray) # stacks images horizontally
        ver = hor # as standardization 
    return ver

img = cv2.imread('Resources/lena.png')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # apply greyscale to image

imgStack = stackImages(0.5,([img,imgGray,img],[img,img,img])) # row, second coloumn row

# imgHor = np.hstack((img,img)) # stacking images horizontally
# imgVer = np.vstack((img,img)) # stacking images vertically
#
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
cv2.imshow("ImageStack",imgStack)

cv2.waitKey(0)
