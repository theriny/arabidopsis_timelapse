# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 16:59:27 2017

@author: theri
"""
import numpy as np
import cv2
import os

os.chdir('c:/Python27/Trevor_timelapse/4_10')

mask = cv2.imread('array.jpg',0)
im = cv2.imread('frame322.jpg')
gray_img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

#create NumPy arrays from the color gray boundaries
#low = np.array([89-20, 82-20, 75-20])
#high = np.array([255, 255, 255])


#find the colors within the specified boundaries and apply the mask

mask_inv = 255 - mask
output = cv2.bitwise_and(gray_img, gray_img, mask = mask) #using this is key to applying a single mask to multiple images





#filter out the noise
kernel = np.ones((2,2),np.uint8)
opening = cv2.morphologyEx(output,cv2.MORPH_OPEN,kernel, iterations = 6)

#use erosion to skeletonize the image (edges)
erode = cv2.erode(opening, kernel, iterations = 5)
cv2.imshow('eroded', erode)
cv2.waitKey(0)

image,contours,hierarchy = cv2.findContours(erode,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(im, contours, -1, (0,255,0), 3)
cv2.imshow('contours', img)
cv2.waitKey(0)
