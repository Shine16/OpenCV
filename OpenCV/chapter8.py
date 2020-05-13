import cv2
import numpy as np

# detecting shapes
#https://realpython.com/python-idle/


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver



def getContours(img):
    
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    # all contours are saved in contours
    
    for cnt in contours:
        # each contour in cnt
        area = cv2.contourArea(cnt) # find area of contour
        print(area)
        if area>500: # > 500 pixels, threshold for area so it does not detect noise
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) #draw contour in blue, image, contour, index, blue, line width
            peri = cv2.arcLength(cnt,True) # calculates contour perimeter
            #print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            #https://docs.opencv.org/3.4.8/d3/dc0/group__imgproc__shape.html#ga0012a5fdaea70b8a9970165d98722b4c
            # https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html
            #https://answers.opencv.org/question/74777/how-to-use-approxpolydp-to-close-contours/
            #https://rsdharra.com/blog/lesson/16.html
            #https://theailearner.com/2019/11/22/simple-shape-detection-using-contour-approximation/
            #https://docs.opencv.org/3.4/dc/dcf/tutorial_js_contour_features.html
            #https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#ga0012a5fdaea70b8a9970165d98722b4c
            #https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm
            #finds number of corners , true - contour is closed
            #Image ApproxPolyDP Example
                #https://docs.opencv.org/3.4/js_contour_features_approxPolyDP.html

                #OpenCV: Structural Analysis and Shape Descriptors
                #https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#ga0012a5fdaea70b8a9970165d98722b4c

            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx) #use bounding box to get dimensions of object

            if objCor ==3:
                objectType ="Tri"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio >0.98 and aspRatio <1.03:
                    objectType= "Square"
                else:
                    objectType="Rectangle"
            elif objCor>4:
                objectType= "Circles"
            else:
                objectType="None"


            
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2) # draw bounding box, green
            
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2)# place text




path = 'Resources/shapes.png'
img = cv2.imread(path)
imgContour = img.copy() # copy over

#preprocessing
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #grayscale
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1) #blur it, why? make it thicker??
imgCanny = cv2.Canny(imgBlur,50,50) #canny edge detection
#imgCanny = cv2.Canny(imgGray,50,50)
getContours(imgCanny) # get the contours

imgBlank = np.zeros_like(img)
imgStack = stackImages(0.8,([img,imgGray,imgBlur],
                            [imgCanny,imgContour,imgBlank]))

cv2.imshow("Stack", imgStack)

cv2.waitKey(0)
