# HSV rather than BGR , invented in 1970s
# Hue (Color) Saturation (how pure) Value (bright)


import cv2
import numpy as np

frameWidth = 640*2/3
frameHeight = 480*2/3

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

#function it will call?
def empty(a):
    #print("yo")
    pass

# create window, resize and create trackbars
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,245)
cv2.createTrackbar("HUE Min","HSV",0,255,empty) #starting value, total bar count, function called when changed
cv2.createTrackbar("HUE Max","HSV",255,255,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VAL Min","HSV",0,255,empty)
cv2.createTrackbar("VAL Max","HSV",255,255,empty)


while True:
    _, img = cap.read() # read returns retval, image

    # convert to HSV colorspace
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # functions to get track bar values
    h_min = cv2.getTrackbarPos("HUE Min", "HSV")
    h_max = cv2.getTrackbarPos("HUE Max", "HSV")
    s_min = cv2.getTrackbarPos("SAT Min", "HSV")
    s_max = cv2.getTrackbarPos("SAT Max", "HSV")
    v_min = cv2.getTrackbarPos("VAL Min", "HSV")
    v_max = cv2.getTrackbarPos("VAL Max", "HSV")
    #print(h_min)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    imgMask = cv2.inRange(imgHsv, lower , upper)
    imgResults = cv2.bitwise_and(img , img, mask = imgMask) # using mask function of bitwise and

    # Mask is 1 channel, needs to be 3 to stack with rest
    imgMask = cv2.cvtColor(imgMask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img,imgMask,imgResults])

    #cv2.imshow('Original',img)
    #cv2.imshow('HSV Colorspace',imgHsv)
    #cv2.imshow('Mask', imgMask)
    #cv2.imshow('Results',imgResults)
    cv2.imshow('Stacked', hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()