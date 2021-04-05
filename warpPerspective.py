import cv2
import numpy as np
import math
import time

new_imgH = 512
fov = 0.5 * math.pi
CENTERx = 45 * math.pi / 180
CENTERy = -0 * math.pi / 180

def imgSphere2Perspective(im, CENTERx, CENTERy, new_imgH, fov):

    sphereW = im.shape[1]
    sphereH = im.shape[0]

    TXwarp, TYwarp = np.meshgrid(np.arange(1, new_imgH+1, 1), np.arange(1, new_imgH+1, 1))
    TX = TXwarp.transpose(1, 0).flatten().reshape(-1, 1)
    TY = TYwarp.transpose(1, 0).flatten().reshape(-1, 1)
    TX = TX - 0.5 - new_imgH / 2
    TY = TY - 0.5 - new_imgH / 2

    r = (new_imgH / 2) / (np.tan(fov / 2))
    R = np.sqrt(np.power(TY, 2) + np.power(r, 2))
    ANGy = np.arctan((- TY)/r) + CENTERy

    X = np.sin(ANGy) * R
    Y = - np.cos(ANGy) * R
    Z = TX

    ANGx = np.arctan(Z / (- Y))

    start = time.time()
    for i in range(len(ANGy)):
        if np.abs(ANGy[i, 0]) > math.pi/2:
            ANGx[i, 0] = ANGx[i, 0] + math.pi

    RZY = np.sqrt(np.power(Z, 2) + np.power(Y, 2))
    ANGy = np.arctan(X/RZY)
    ANGx = ANGx + CENTERx

    for i in range(len(ANGy)):
        if ANGy[i, 0] < - math.pi/2:
            ANGy[i, 0] = - ANGy[i, 0] - math.pi
            ANGx[i, 0] = ANGx[i, 0] + math.pi
        if ANGx[i, 0] <= - math.pi:
            ANGx[i, 0] = ANGx[i, 0] + 2 * math.pi
        if ANGx[i, 0] > math.pi:
            ANGx[i, 0] = ANGx[i, 0] - 2 * math.pi

    end = time.time()
    print(end - start)

    Px = (ANGx + math.pi) / (2 * math.pi) * sphereW + 0.5
    Py = ((- ANGy) + math.pi / 2) / math.pi * sphereH + 0.5

    for i in range(len(Px)):
        if Px[i, 0] < 1:
            Px[i, 0] = Px[i, 0] + sphereW

    # This part used to add external columns to origin image
    col1 = im[:, 0, :].reshape(-1, 1, 3)
    col2 = im[:, 1, :].reshape(-1, 1, 3)
    im = np.column_stack((im, col1))
    im = np.column_stack((im, col2))

    Px = Px.reshape((new_imgH, new_imgH), order = 'F')
    Py = Py.reshape((new_imgH, new_imgH), order = 'F')

    minX = int(max(0, np.floor(Px.min()) - 2))
    minY = int(max(0, np.floor(Py.min()) - 2))

    maxX = int(min(im.shape[1], np.ceil(np.max(Px))))
    maxY = int(min(im.shape[0], np.ceil(np.max(Py))))

    im = im[minY:maxY, minX:maxX]

    Px = Px.astype('float32')
    Py = Py.astype('float32')

    im = cv2.remap(im, Px - minX + 1, Py - minY + 1, cv2.INTER_LINEAR)

    return im

start1 = time.time()
img = cv2.imread('grdView.jpg')
end1 = time.time()

start2 = time.time()
dst = imgSphere2Perspective(img, CENTERx, CENTERy, new_imgH, fov)
end2 = time.time()

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.imwrite('fov90-x0-y0.jpg', dst)
print((end1-start1))
print((end2-start2))


















