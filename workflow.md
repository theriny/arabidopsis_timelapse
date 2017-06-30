#Measuring Time-Lapsed Canopy Area of Arabidopsis Plants via Python OpenCV Image Analysis


#Part 1: Selecting the Trays
##Step 1 : Load Required Libraries

> import os
import cv2
import numpy as np
import argparse

##Step 2: Set the working directory (Image Location)

> os.chdir('c:/Python27/Trevor_timelapse/3_24')

##Step 3: Read the image into a variable

> img = cv2.imread('frame3.jpg')

##Step 4: Define boundaries for the color gray in the BGR colorspace (create NumPy array from the boundaries)

> low = np.array([128, 128, 128])
high = np.array([224, 224, 224])

##Step 5: Find colors within the specified boundaries and apply the mask

>mask = cv2.inRange(img, low, high)
output = cv2.bitwise_and(img, img, mask = mask)

##Step 6: Filter noise

> kernel = np.ones((2,2),np.uint8)
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel, iterations = 4)

##Step 7: Erode the image for skeletonization

> erode = cv2.erode(opening, kernel, iterations = 5)
> cv2.imshow("image",erode)
cv2.waitKey(0)

##Step 8: Detect edges of the eroded (skeletonized) image

> edges = cv2.Canny(erode, 150, 450, apertureSize = 3)
cv2.imshow("edges", edges)
cv2.waitKey(0)

##Step 9: Use Houghlines to detect lines from the edges image

>lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

> 	for rho, theta in lines[0]:
    	a = np.cos(theta)
    	b = np.sin(theta)
    	x0 = a * rho
    	y0 = b * rho
    	x1 = int(x0 + 1000*(-b))
    	y1 = int(y0 + 1000*(a))
    	x2 = int(x0 - 1000*(-b))
    	y2 = int(y0 - 1000*(a))

    >cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)

>cv2.imwrite('houghlines3.jpg', img)



