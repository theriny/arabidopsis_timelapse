# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 14:11:08 2017

@author: theri
"""
from matplotlib import pyplot as plt
import numpy as np
import cv2
import os, os.path
import argparse #used for image rotation
import imutils
import math
import glob

os.chdir('c:/Python27/Trevor_timelapse/3_24')

frames = glob.glob('./*.jpg')
angle_list = []
for frame in frames:
    def angles(arg):
        img = cv2.imread(arg)
    
        low = np.array([89-20, 82-20, 75-20])
        high = np.array([207+20, 206+20, 212+20])
        mask = cv2.inRange(img, low, high)
        #output = cv2.bitwise_and(img, img, mask = mask)
        kernel = np.ones((2,2),np.uint8)
        opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel, iterations = 4)
        erode = cv2.erode(opening, kernel, iterations = 5)
        edges = cv2.Canny(erode, 150, 450, apertureSize = 3)
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

            cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1) 
        
            if (x1 == x2):
                slope = 90
            else:
                slope = ((y2 - y1) / (x2 - x1))
        
        theta = math.degrees(math.atan(slope))
        angle = 90 - theta
        angle_list.append(angle)     
        print angle
        np.hstack(angle_list)
       
    angles(frame)
    
    



    
    
    