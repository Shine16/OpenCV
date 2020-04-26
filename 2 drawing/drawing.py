import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)

#start, end, color RGB, line width
cv2.line(img,(10,10),(100,150),(255,255,255),3)

#top left, bottom right, color RGB, line thickness
cv2.rectangle(img,(10,10),(250,120),(0,120,255),4)

#center, radius, color, width (-1 is filled)
cv2.circle(img,(125,60), 30, (0,255,0), -1)

pts = np.array([[50,10],[70,80],[60,120],[30,60]], np.int32)
#pts = pts.reshape((-1,1,2))# OpenCV documentation had this code, which reshapes the array to a 1 x 2. I did not  find this necessary, but you may:
cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(10,150), font, 1, (200,255,155), 2, cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
