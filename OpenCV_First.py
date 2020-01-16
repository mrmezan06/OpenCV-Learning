import numpy as np
import cv2
import matplotlib.pyplot as plot

# cv2.IMREAD_GRAYSCALE is simply remove alpha from RGBA simply call transparency
img = cv2.imread('akash.jpg', cv2.IMREAD_GRAYSCALE)
# print(img)

# cv2.imshow('Image', img)
# 0 means no delay wait for any key press
# other number it is destroy after this time automatically
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# plot.imshow(img, cmap='gray', interpolation='bicubic')
# plot.plot([50, 100], [80, 100], 'c', linewidth=5)
# plot.show()
# saving image
# cv2.imwrite('akashgrey.jpg', img)
