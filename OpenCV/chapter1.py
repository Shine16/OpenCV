#intro
# array of boxes, pixels, vga is 640x480 , hd is 1280x720
# binary image, only black and white , 0 and 1
# grayscake is 0-255 value in each pixel
# RGB is made of R G and B



######################## READ IMAGE ############################
##import cv2
## # LOAD AN IMAGE USING 'IMREAD'
##img = cv2.imread("Resources/lena.png")
## # DISPLAY
##cv2.imshow("Lena Soderberg",img)
##cv2.waitKey(0)

######################### READ VIDEO #############################
##import cv2
##frameWidth = 640
##frameHeight = 480
##cap = cv2.VideoCapture("Resources/test_video.mp4")
##while True:
##    success, img = cap.read()
##    try:
##        img = cv2.resize(img, (frameWidth, frameHeight))
##        cv2.imshow("Result", img)
##    except:
##        print("error")
##        cap = cv2.VideoCapture("Resources/test_video.mp4")    
##    if cv2.waitKey(1) & 0xFF == ord('q'):
##        cap = cv2.VideoCapture("Resources/test_video.mp4")
##        #break
##    
######################### READ WEBCAM  ############################
import cv2


frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0) #0 for webcam
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
#https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html
#https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a5d5f5dacb77bbebdcbfb341e3d4355c1
#OpenCV 3 Computer Vision with Python Cookbook: Leverage the power of OpenCv
#https://www.programcreek.com/python/example/85663/cv2.VideoCapture



cap.set(3, frameWidth) # width id is 3
cap.set(4, frameHeight) # height id is 4
cap.set(10,150) # brightness id is 10
# id is property enumerator from here https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
