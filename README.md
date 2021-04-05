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
