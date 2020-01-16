import numpy as np
import cv2

img = cv2.imread('akash.jpg', cv2.IMREAD_COLOR)
px = img[55, 55]
print(px)
# 1PX
# img[55, 55] = [0, 0, 255]
# Region of Image
# roi = img[100:150, 100:150]
# print(roi)
# ROI is fill with green color
# img[100:150, 100:150] = [0, 255, 0]

# Replacing image from ROI
face = img[200:400, 200:500]
img[300:500, 200:500] = face
cv2.imshow('Override', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
