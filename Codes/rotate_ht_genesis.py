# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 10:14:53 2017

@author: theri
"""

import cv2
import os, os.path
from sys import argv

script, filename, angle = argv



os.chdir('c:/Python27/Trevor_timelapse/')


img = cv2.imread(filename)
#cv2.imshow('original', img)
#cv2.waitKey(0)
 


rows,cols = img.shape[:2]
M = cv2.getRotationMatrix2D((cols/2, rows/2),-float(angle),1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.namedWindow('rotated', cv2.WINDOW_NORMAL)
cv2.imshow('rotated', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
