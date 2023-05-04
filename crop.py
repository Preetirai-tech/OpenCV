import cv2

import os

img = cv2.imread(os.path.join('.', 'data', 'cloud.jpg'))
cropped_img = img[800:2000, 800:2000]

print(cropped_img.shape)
cv2.imshow('image', cropped_img)
cv2.waitKey(0)