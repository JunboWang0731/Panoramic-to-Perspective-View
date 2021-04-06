import cv2
import numpy as np
import math
import time

img = cv2.imread('grdView.jpg')

start = time.time()

# s means height and width of dst image, which size is s*s pixels
# fov means field of view(in radius)
# Ch means cemera height from image plane(in pixels)
s = 1200
fov = 0.95 * math.pi
Ch = s / 2 / np.tan(fov/2)
H = img.shape[0]
W = img.shape[1]

Y, X = np.meshgrid(np.arange(0, s, 1), np.arange(0, s, 1))

#theta generate from arctan2 is in range (-pi, pi). theta should add 2*pi for Y > s/2 so it ranged from (0, pi)
theta = np.arctan2(s/2 - Y, X - s/2)
theta[:, int(s/2)+1:s] = theta[:, int(s/2)+1:s] + 2 * math.pi
r = np.sqrt(np.power((s/2 - Y), 2) + np.power((s/2 - X), 2))

# in opencv the point(x, y) means it locate at x_th column and y_th row
Py = H - np.arctan(r / Ch) * H / math.pi
Px = W / (2 * math.pi) * theta

Px = Px.astype('float32')
Py = Py.astype('float32')
dst = cv2.remap(img, Px, Py, cv2.INTER_LINEAR)

end = time.time()

cv2.imshow('Origin', img)
cv2.imshow('Destination', dst)
cv2.imwrite('grdViewOwnMethod.jpg', dst)
cv2.waitKey(0)
print("Time consuming on remapping: %f seconds: " % (end - start))