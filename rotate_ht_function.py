# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 13:12:13 2017

@author: theri
"""

import cv2
import os, os.path
import glob


os.chdir('c:/Python27/Trevor_timelapse/3_24')
dirname = 'C:/Python27/Trevor_timelapse/rotated'
os.mkdir(dirname)
angles_file = open("c:/Python27/Trevor_timelapse/3_24/angles.txt", "r")
angles_list = angles_file.readlines()
frames = glob.glob('./*.jpg')

with open("c:/Python27/Trevor_timelapse/3_24/angles.txt", "r") as a:
    count = 0
    for frame in frames:
        for angle in a:
                def rotate_image(arg1, arg2):
                    img = cv2.imread(arg1)
                    rows,cols = img.shape[:2]
                    M = cv2.getRotationMatrix2D((cols/2, rows/2),-float(arg2),1)
                    dst = cv2.warpAffine(img,M,(cols,rows))                
                    cv2.imwrite(os.path.join(dirname, "frame%d.jpg" % count), dst)
                count += 1               
                rotate_image(frame, angle)