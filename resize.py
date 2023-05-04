import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'lena.jpg'))


#cv2.imshow('Image', img)
resized_img = cv2.resize(img, (250,250))

print(resized_img.shape)

cv2.imshow('image', resized_img)
cv2.waitKey(0)