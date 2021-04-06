import cv2
import numpy as np
import math

img = cv2.imread('001305.jpg')
s = img.shape[0]
H = 256 * np.sqrt(2)
W = 1664

Y, X = np.meshgrid(np.arange(0, W, 1), np.arange(0, H, 1))
theta = 2 * math.pi * Y / W

# in opencv the point(x, y) means it locate at x_th column and y_th row
Py = s/2 + (H - X - 1) * np.cos(theta)
Px = s/2 - (H - X - 1) * np.sin(theta)

Px = Px.astype('float32')
Py = Py.astype('float32')

dst = cv2.remap(img, Px, Py, cv2.INTER_LINEAR)

cv2.imshow('hi', img)
cv2.imshow('dst', dst)
cv2.imwrite('polartransform.jpg', dst)
cv2.waitKey(0)