# A. Defining the colorspace for the plant trays

In this part of the process we want to tell the machine to identify only the pixels that make up the visible borders of the plant trays. This is important because in some images the plant trays are slightly rotated which may cause difficulty when segmenting pots later. The color of the trays is a grayish color which varies depending on the surrounding lighting (time of day).

Therefore, in order to identify upper and lower thresholds for the shades of gray, sample images were imported into Matlab, and the sample pixels of interest were manually selected using the following MatLab code.
```matlab
I = imread('image');
impixel(I);
```
The command,**'impixel'**, allows the user to manully select pixels of an image. After selecting pixels, a list of RGB values for the selected pixels is displayed to the user. The RGB values were then imported into EXCEL. Because a bright and dark image was used to gather pixel data, the maxima for the R, G, B values of the bright image serve as the upper threshold and the minima of the dark image serve as the lower threshold for RGB values that represent pixels of the plant trays.

# B. Finding the possible skew angle of the plant trays

Now that we know the range of RGB values for the gray plant trays, we can tell the machine to only focus on those pixels whithin this range. If we can detect a line from the chosen pixels, we can also find the slope of that line which can then tell us something about the skew angle. Once the skew angle is calculated, we can rotate the image by the skew angle so that the edges of the plant trays are completely vertical and horizontal.

###Objectives
1. Input image
2. Detect lines (Hough Lines)
2. Output skew angle of line

###Code
**1. Load required packages/libraries**
```Python
import os, os.path
import cv2
import numpy as np
import math
import glob
```

* "os" is module for path name manipulation
* "cv2" is module for computer vision library
* "np" is module for scientific computing
* "math" is module for mathematic functions
* "glob" is module that finds pathnames matching a pattern

**2. Set the working directory to where images are located**
```Python
os.chdir('c:/Python27/Trevor_timelapse/3_24')
```
* "os.chdir" changes the current directory the the one in parenthesis

**3. Create variable for the images we want to analyze using "glob" module**
```Python
frames = glob.glob('./*.jpg')
```
**4. Create list to store calculated angles**
```Python
angle_list = []
```
**5. Loop through the frame images, Define the angles function, Detect lines, Find slope of lines**

Loop through the frame images
```Bash
for frame in frames:
```
Define the function "angles" and its argument "arg"   
   ```Python
    def angles(arg):
    ```
   
   Read in image
   ```Python
        img = cv2.imread(arg)
   ```
        
   Define upper and lower thresholds for RGB values of plant tray pixels and create mask
   ```Python
        low = np.array([89-20, 82-20, 75-20])
        high = np.array([207+20, 206+20, 212+20])
        mask = cv2.inRange(img, low, high)
        ```
        
        
  Remove noise from the binary image
   ```Python
        kernel = np.ones((2,2),np.uint8)
        opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel, iterations = 4)
        erode = cv2.erode(opening, kernel, iterations = 5)
        ```
  
  Detect edges of the eroded binary image and use Hough Lines to detect lines from the edges
 ```Python
        edges = cv2.Canny(erode, 150, 450, apertureSize = 3)
        lines = cv2.HoughLines(edges, 1, np.pi/180, 2)
        ```
        
   Define equations for a detected line
 ```Python
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
        ```
            
   Calculate slope of the line
   ```Python
            if (x1 == x2):
                slope = 90
            else:
                slope = ((y2 - y1) / (x2 - x1))
                ```
   Use slope to calculate the skew angle     
   ```Python     
        theta = math.degrees(math.atan(slope))
        angle = 90 - theta
        angle_list.append(angle)     
        print angle
        np.hstack(angle_list)
        np.savetxt('angles.txt', angle_list)
```




