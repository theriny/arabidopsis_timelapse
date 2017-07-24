## In the previous "angle_ht_function" code, the skew angles for each of the original images passed through the for loop were saved in a text file. This code calls on that text file and inputs the skew angle into a rotate command (cv2.getRotationMatrix2D) which then rotates the image and corrects for the skew angle.

Import libraries

```Python
import cv2
import os, os.path
import glob
```
Set directory to where the images are located
```Python
os.chdir('c:/Python27/Trevor_timelapse/3_24')

```

Create a folder where the rotated images will be saved
```Python
dirname = 'C:/Python27/Trevor_timelapse/rotated'
os.mkdir(dirname)
```

Open and read the text file containing the previously saved skew angles. Read the skew angles into a list.
```Python
angles_file = open("c:/Python27/Trevor_timelapse/3_24/angles.txt", "r")
angles_list = angles_file.readlines()
```

Create variable for the images we want to analyze using "glob" module
```Python
frames = glob.glob('./*.jpg')
```

