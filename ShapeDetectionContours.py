import cv2
import numpy as np
import myUtilities

frameWidth = 640
frameHeight = 400
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold 1", "Parameters", 150,255,empty) # empty is called when there is change in value
cv2.createTrackbar("Threshold 2", "Parameters", 255,255,empty)
cv2.createTrackbar("Area", "Parameters", 5000,30000,empty)

def getContours(img,imgContour):#image in, display contour
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)# CHAIN_APPROX_SIMPLE will have less points


    # try detect area in contours to eliminate small ones
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("Area","Parameters")
        
        if area > areaMin:
            cv2.drawContours(imgContour, contours , -1, (255,0,255),7)
            #perimeter
            peri = cv2.arcLength(cnt,True)
            # if contour is closed,
            approx = cv2.approxPolyDP(cnt, 0.02 * peri , True )
            print(len(approx))

            # find points for bounding box
            x_ , y_, w, h = cv2.boundingRect(approx)
            # draw bounding box
            cv2.rectangle(imgContour, (x_,y_), (x_ + w , y_+ h),(0,255,0),5)

            # write text to image
            cv2.putText(imgContour, "Points: " +str(len(approx)), (x_ + w + 20 , y_ + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), 2)
            cv2.putText(imgContour, "Areas: " + str(int(area)), (x_ + w + 20, y_ + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)





while True:
    success, img = cap.read()

    # Blur, then Grayscale
    imgBlur = cv2.GaussianBlur(img,(7,7),1) # smoothen out ?
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY) # better for canny image?

    threshold1 = cv2.getTrackbarPos("Threshold 1","Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold 2", "Parameters")
    imgCanny = cv2.Canny(imgGray,threshold1,threshold2)

    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1) # dialate to make easier for contour function

    imgContour = img.copy()
    getContours(imgDil, imgContour)

    imgStack = myUtilities.stackImages(0.8,([img, imgBlur, imgGray],[imgCanny, imgDil, imgContour]))

    cv2.imshow("Result", imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
