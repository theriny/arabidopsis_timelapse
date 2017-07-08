# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 16:59:27 2017

@author: theri
"""
import numpy as np
import cv2
import os

os.chdir('c:/Python27/Trevor_timelapse/rotated')


im = cv2.imread('frame1.jpg')

#create NumPy arrays from the color gray boundaries
low = np.array([89-20, 82-20, 75-20])
high = np.array([255, 255, 255])


#find the colors within the specified boundaries and apply the mask
mask = cv2.inRange(im, low, high)
output = cv2.bitwise_and(im, im, mask = mask)

#filter out the noise
kernel = np.ones((2,2),np.uint8)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel, iterations = 4)

#use erosion to skeletonize the image
erode = cv2.erode(opening, kernel, iterations = 5)
cv2.imshow('eroded', erode)
cv2.waitKey(0)

image,contours,hierarchy = cv2.findContours(erode,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
cv2.imshow('contours', img)
cv2.waitKey(0)
