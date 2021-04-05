# Panoramic-to-Perspective-View
Python implementation of the MATLAB implementation of "3D Geometry for Panorama" by Jianxiong Xiao.

# Environments
python 3.7

opencv-python

numpy

# Usage
$new_imgH$ is the length and width of perspective image (new_imgH * new_imgH), the unit is pixels

$fov$ is field of view, which is in radius

$CENTERx, CENTERy$ decide the angle of view, x axis points to bottum of camera and y axis points to right side of camera. (0, 0) means optical axis camera towards center of panoramic image.

The panoramic image(from CVACT dataset)
![grdView](https://user-images.githubusercontent.com/35421034/113550288-6b1dbf00-9625-11eb-9fe2-9ac3fbafbb92.jpg)

The percpective view of fov90 at (CENTERx:0, CENTERy:0)
![fov90-x0-y0](https://user-images.githubusercontent.com/35421034/113550235-53ded180-9625-11eb-9f45-f836118da338.jpg)

The percpective view of fov90 at (CENTERx:45, CENTERy:0)
![fov90-x0-y0](https://user-images.githubusercontent.com/35421034/113550393-92748c00-9625-11eb-976c-835e8b0492c3.jpg)

The percpective view of fov90 at (CENTERx:45, CENTERy:-45)
![fov90-x0-y0](https://user-images.githubusercontent.com/35421034/113550463-ad470080-9625-11eb-8b96-164dc7e64205.jpg)



