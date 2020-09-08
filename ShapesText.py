import cv2
import numpy as np

#img = np.zeros((512,512)) # only black and white / grayscale
img = np.zeros((512,512,3)) #color
print(img) #is float

img = np.zeros((512,512,3),np.uint8) #we want 8 bit integers
print(img)

#img[20:30,200:250] = 255 , 0 , 0 # changes blue selectively
#img[:] = 255 , 0 , 0 # changes all first matrix (blue) to 255, [:] for whole image

#cv2.line(img,(0,0),(100,100),(0,255,0),2)# from , to , color , thickness
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2)# from , to (using image variables), color

cv2.rectangle(img,(350,100),(450,200),(0,0,255),cv2.FILLED) # from, to, color, filled

cv2.circle(img,(150,400),50,(255,0,0),3)#starting point, radius, color, thickness

cv2.putText(img,"Draw Shapes",(75,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1) #text, starting pos, font, font scale, color, thickness


cv2.imshow("Image",img)

cv2.waitKey(0)

