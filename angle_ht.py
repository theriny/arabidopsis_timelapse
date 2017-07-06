# load the required libraries
import os
import cv2
import numpy as np
import argparse
import math


#set the working directory to where the raw image is located
os.chdir('c:/Python27/Trevor_timelapse/3_24')

# import the image
img = cv2.imread('frame4.jpg')


#Define the boundaries for the color gray in the BGR colorspace (OpenCV represents images as NumPy arrays in reverse order)
#each entry in the list is a tuple with two values:a lsit of lower limits and a list of upper limits
#create NumPy arrays from the color gray boundaries
low = np.array([89-20, 82-20, 75-20])
high = np.array([207+20, 206+20, 212+20])


#find the colors within the specified boundaries and apply the mask
mask = cv2.inRange(img, low, high)
output = cv2.bitwise_and(img, img, mask = mask)

#filter out the noise
kernel = np.ones((2,2),np.uint8)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel, iterations = 4)

#use erosion to skeletonize the image
erode = cv2.erode(opening, kernel, iterations = 5)

# show the image
cv2.imshow("image",erode)
cv2.waitKey(0)

# detect edges of the eroded (skeletonized) image
edges = cv2.Canny(erode, 150, 450, apertureSize = 3)
cv2.imshow("edges", edges)
cv2.waitKey(0)

#create a variable for the lines that will be created using the HoughLines function
lines = cv2.HoughLines(edges, 1, np.pi/180, 2)

#for x in range(0, len(lines)):
for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
        
    if (x1 == x2):
        slope = 90
    else:
        slope = ((y2 - y1) / (x2 - x1))

# find the angle of the found line
theta = math.degrees(math.atan(slope))
angle = 90 - theta
print angle



