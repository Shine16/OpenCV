import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
print(kernel)

path = "Resources\lena.png"
#img = cv2.imread(path,0) # 0 for grayscale
img = cv2.imread(path)



cv2.imshow("Lena",img) #window name, image


#Grayscale
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("LenaGray",imgGray)

#Blur
#higher value higher blur, need to be odd number
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
cv2.imshow("LenaBlur",imgBlur)

#Edge detection
#value differs for images
imgCanny = cv2.Canny(imgBlur,100,100)
cv2.imshow("LenaBlur",imgCanny)

#Dilation
#more iterations, more effect, thicker lines
imgDilation= cv2.dilate(imgCanny,kernel, iterations=1)
cv2.imshow("LenaDialation",imgDilation)

#Errosion
#thinner line, opposite of dilation
imgEroded = cv2.erode(imgDilation, kernel , iterations = 1)
cv2.imshow("LenaEroded",imgEroded)


cv2.waitKey(0)