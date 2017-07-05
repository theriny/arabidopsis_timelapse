# load the required libraries
import os
import cv2
import numpy as np
import argparse


#set the working directory to where the raw image is located
os.chdir('c:/Python27/Trevor_timelapse/3_24')

# import the image
img = cv2.imread('frame3.jpg')

#convert image to hsv colorspace
#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)




#Define the boundaries for the color gray in the BGR colorspace (OpenCV represents images as NumPy arrays in reverse order)
#each entry in the list is a tuple with two values:a lsit of lower limits and a list of upper limits


#create NumPy arrays from the boundaries
low = np.array([128-10, 128-10, 128-10])
high = np.array([224+10, 224+10, 224+10])


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

for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)



    cv2.imwrite('houghlines3.jpg', img)

# find the angle of the line
slope = ((y2 - y1)/(x2 - x1))
angle = 

'''
#gray the (x,y) coordinates of all pixel values that are greater than zero,
#then use these coordinates to compute a rotated bounding box that contans all
#coordinates


coords = np.column_stack(np.where(edges > 0))
angle = cv2.minAreaRect(coords)[-1]

#add 90 degrees to the angle

if angle < -45:
    angle = -(90 + angle)

#otherwise,just take the inverse of the angle to make it positive
else: angle = -angle

# rotate the image to deskew it
(h, w) = edges.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated = cv2.warpAffine(edges, M, (w, h),
    flags = cv2.INTER_CUBIC, borderMode = cv2.BORDER_REPLICATE)

# draw the correction angle on the image so we can validate it
cv2.putText(rotated, "Angle: {:.2f} degrees".format(angle), (10, 30),
    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

#show the output image
print ("[INFO] ANGLE: {:.3F}".format(angle))
cv2.imshow("Input", edges)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
'''
