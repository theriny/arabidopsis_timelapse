# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 13:12:13 2017

@author: theri
"""

import cv2
import os, os.path
import glob
from angle_ht_long import angle_list

os.chdir('C:/Users/theriny/Dropbox/Trevor_timelapse/extracted_frames3')
dirname = 'C:/Users/theriny/Dropbox/Trevor_timelapse/extracted_frames3/rotated'
os.mkdir(dirname)
frames = glob.glob('./*.jpg')

count = 0
while (count < len(frames)):
    for frame in frames:
        for angle in angle_list:
            def rotate_image(arg1, arg2):
                img = cv2.imread(arg1)
                rows,cols = img.shape[:2]
                M = cv2.getRotationMatrix2D((cols/2, rows/2),-float(arg2),1)
                dst = cv2.warpAffine(img,M,(cols,rows))
                cv2.imwrite(os.path.join(dirname, "frame%d.jpg" % count), dst)
        count += 1
            
        rotate_image(frame, angle)
