import numpy as np
import cv2
import matplotlib.pyplot as plot

img = cv2.imread('akash.jpg', cv2.IMREAD_COLOR)
# Color System in CV2 BGR
# cv2.line(img, (0, 0), (200, 200), (0, 255, 0), 15)
# rectangle(image, startpt1(x,y), Drawpt2(x,y), BGR(255,255,255),linewidth)
cv2.rectangle(img, (100, 200), (450, 600), (0, 255, 0), 10)
cv2.circle(img, (450, 200), 55, (0, 0, 255), -1)
cv2.imshow('Line Draw', img)
cv2.waitKey(0)
cv2.destroyAllWindows()