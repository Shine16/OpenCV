# good for one pipeline and see iteration of each image
# images can use matplot
# video will be slow if matplot , has special function

# !! stacking needs both images to be same height, width, channels
# Ctrl+Shift+/ . for block comment
import cv2
import numpy as np
import myUtilities
#from Resources import myUtilities # if myUtilities is in Resources

'''
#special function to stack , shifted to myUtilities
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
'''

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0) #camera at 0

while True:

    #for webcam
    success, img = cap.read()
    img = cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("video",img)

    kernel = np.ones((5,5),np.uint8)
    #print(kernel)

    # for image
    #img = cv2.imread("Resources/lena.png" , 0) #image imported as a grayscale , 0 channels
    #img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR) # need to make gray to bgr to fit other 3 channel images if used
    #img = cv2.imread("Resources/lena.png" )

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
    imgCanny = cv2.Canny(imgBlur,100,200)
    imgDilation= cv2.dilate(imgCanny,kernel, iterations=2)
    imgEroded = cv2.erode(imgDilation, kernel , iterations = 2)

    imgBlank = np.zeros((100,100),np.uint8)

    # scale , stacked images horizontal, stacked image vertical

    # 3 images
    #StackedImages = stackImages(0.5,([img,imgGray,imgBlur])) # for vertical

    # 3x2 images
    #StackedImages = stackImages(0.5,([img,imgGray,imgBlur],[imgCanny,imgDilation,imgEroded]))

    # with one blank
    #StackedImages = stackImages(0.5,([img,imgGray,imgBlur],[imgCanny,imgDilation,imgBlank])) #function forces image to resize to first image, blank image is resized

    # 6x4 images
    StackedImages = myUtilities.stackImages(0.5, ([img, imgGray, imgBlur,img, imgGray, imgBlur], [imgCanny, imgDilation, imgEroded,imgCanny, imgDilation, imgEroded],[img, imgGray, imgBlur,img, imgGray, imgBlur], [imgCanny, imgDilation, imgEroded,imgCanny, imgDilation, imgEroded]))

    cv2.imshow("Display", StackedImages)


    """ 
    #successfully stacked using numpy functions , not very efficient
    print(img.shape)
    print(imgGray.shape)
    print(imgBlur.shape)
    print(imgCanny.shape)
    print(imgDilation.shape)
    print(imgEroded.shape)
    
    imgGray = cv2.cvtColor(imgGray,cv2.COLOR_GRAY2BGR)
    imgBlur = cv2.cvtColor(imgBlur,cv2.COLOR_GRAY2BGR)
    imgCanny = cv2.cvtColor(imgCanny,cv2.COLOR_GRAY2BGR)
    imgDilation = cv2.cvtColor(imgDilation,cv2.COLOR_GRAY2BGR)
    imgEroded = cv2.cvtColor(imgEroded,cv2.COLOR_GRAY2BGR)
    
    hor1= np.hstack((img,imgGray,imgBlur))
    hor2= np.hstack((imgCanny,imgDilation,imgEroded))
    ver = np.vstack((hor1,hor2))
    
    print(ver.shape)
    ver = cv2.resize(ver,(int(img.shape[1]*3/2),int(img.shape[0]*2/2))) # resize to half image, rounded up for int, 3 images wide by 2 images height
    print(ver.shape)
    
    cv2.imshow("image",ver)
    """

    #cv2.waitKey(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break