import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)#using numpy to create 512x512 pixel image of 0s (black)
#cv2.imshow("Image",img)
#print(img) # prints image out
#img[:]= 255,0,0 # makes image blue, [:] is all, [200:300 , 100:300] will make only one aprt blue

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)# image, starting point, ending point, color, thickness
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) # image, starting point, ending point, color, thickness(or cv.FILLED)
cv2.circle(img,(400,50),30,(255,255,0),5) # image, center point, radius, color, thickness 
cv2.putText(img," OPENCV  ",(200,200),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,150,0),3) # image, text, origin, font, scale, color, thickness 


cv2.imshow("Image",img)

cv2.waitKey(0)
