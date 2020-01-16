import numpy as np
import cv2
import matplotlib.pyplot as plot

img = cv2.imread('akash.jpg', cv2.IMREAD_COLOR)
# Color System in CV2 BGR
# cv2.line(img, (0, 0), (200, 200), (0, 255, 0), 15)
# rectangle(image, startpt1(x,y), Drawpt2(x,y), BGR(255,255,255),linewidth)
cv2.rectangle(img, (100, 200), (450, 600), (0, 255, 0), 10)
cv2.circle(img, (450, 200), 55, (0, 0, 255), -1)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
cv2.polylines(img, [pts], True, (0, 255, 0), 3)

font  = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpeCV Font Testing!', (100, 230), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow('Line Draw', img)
cv2.waitKey(0)
cv2.destroyAllWindows()