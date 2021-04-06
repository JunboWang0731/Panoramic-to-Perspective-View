#This file is used for polar transform and inverse polar transform
import cv2
import time

GroundImgW = 1441
GroundImgH = 511
AerialSideLength = 512

# From polar to cat (sat to grd)
# sourceImg = cv2.imread('001305.jpg')
#
# start = time.time()
# sourceImg = cv2.rotate(sourceImg, cv2.ROTATE_90_COUNTERCLOCKWISE)
# warpedImg = cv2.warpPolar(sourceImg, (GroundImgH, GroundImgW), (AerialSideLength/2, AerialSideLength/2), AerialSideLength/2, cv2.INTER_LINEAR)
# warpedImg = cv2.rotate(warpedImg, cv2.ROTATE_90_COUNTERCLOCKWISE)
# end = time.time()
#
# cv2.imshow("resultofwarpPolar.jpg", warpedImg)
# cv2.waitKey(0)
# print(end - start)

# From cat to polar(grd to sat)
sourceImg = cv2.imread('grdView.jpg')

start = time.time()
sourceImg = cv2.rotate(sourceImg, cv2.ROTATE_90_CLOCKWISE)
warpedImg = cv2.warpPolar(sourceImg, (AerialSideLength, AerialSideLength), (AerialSideLength/2,AerialSideLength/2), AerialSideLength/2, cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
warpedImg = cv2.rotate(warpedImg, cv2.ROTATE_90_CLOCKWISE)
end = time.time()

cv2.imshow("RecongrdView.jpg", warpedImg)
cv2.waitKey(0)

print(end - start)
cv2.destroyAllWindows()