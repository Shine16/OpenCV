import cv2

frameWidth = 640
frameHeight = 480

#cap = cv2.VideoCapture("D:/Vuze/DONE/Sputnik (2020) [1080p] [WEBRip] [5.1] [YTS.MX]/Sputnik.2020.1080p.WEBRip.x264.AAC5.1-[YTS.MX].mp4")
cap = cv2.VideoCapture(0) #camera at 0
#cap.set(3,frameWidth)
#cap.set(4,frameHeight)


while True:
    success, img = cap.read()
    img = cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


        # control left click item will view to python code