import cv2
import numpy as np
from scipy import ndimage

from Quadrants.quadrants import *
WIDTH = 720
HEIGHT = 480


img = cv2.imread('images/tv12.jpg', 2)
cv2.imshow("original", img)
resized = cv2.resize(img, (WIDTH, HEIGHT), interpolation=cv2.INTER_AREA)
ret, bw_image = cv2.threshold(resized, 60, 1, cv2.THRESH_BINARY_INV)
imgArray = np.asarray(bw_image)

imgArrayFilled = np.array(ndimage.binary_fill_holes(imgArray), dtype=np.uint8) * 255

cv2.imshow("nonfilled", imgArray * 255)
cv2.imshow("filled", imgArrayFilled)
cv2.waitKey(0)
cv2.destroyAllWindows()
