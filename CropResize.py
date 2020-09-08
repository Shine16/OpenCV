import cv2

#crop resize is good for extracting selected areas of image

path = "Resources/lena.png"
img = cv2.imread(path)

# X is positive towards right
# Y is opposite (downwards)

print(img.shape) # prints X , Y, no. of pixels
cv2.imshow("Lena",img)

#resize image smaller or bigger
#width , height = 400,400 #smaller
width , height = 1000,1000 #bigger
imgResize = cv2.resize(img, (width,height))
print(imgResize.shape)
cv2.imshow("Lena Resized", imgResize)

#crop image
imgCropped = img[250:290,250:350] #height, width
cv2.imshow("Lena Cropped", imgCropped)

# resize using original image height width
imCropResize= cv2.resize(imgCropped,(img.shape[1],img.shape[0]))
cv2.imshow("Lena Cropped Resized", imCropResize)



cv2.waitKey(0)