# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 16:05:07 2017

@author: theri
"""

import argparse
import cv2
import os
from PIL import Image


os.chdir('C:/Python27/Trevor_timelapse/rotated')

refPt = []
selection = False
rgb = []

def get_pixel_value(event, x, y, flags, param):
    
    global refPt, selection, rgb
    
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt.append((x,y))
        rgb.append(image[refPt])
        selection = True
        
    elif event == cv2.EVENT_LBUTTONUP:
        selection = False
        
       


 #Get the RGBA Value of the a pixel of an image
image = cv2.imread('frame1.jpg')
im = Image.open("frame1.jpg")
pix = im.load()
clone = im.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", get_pixel_value)

while True:
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):
        image = clone.copy()

    elif key == ord("a"):
        break
        
cv2.destroyAllWindows()

    