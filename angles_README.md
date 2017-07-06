#Defining the colorspace for the plant trays

##In this part of the process we want to tell the machine to identify only the pixels that make up the visible borders of the plant trays. The color of the trays is a grayish color which varies depending on the surrounding lighting (time of day).

##Therefore, in order to identify upper and lower thresholds for the shades of gray, sample images were imported into Matlab, and the sample pixels of interest were manually selected using the following MatLab code.

> I = imread('image');
> impixel(I);

##The command,'impixel', allows the user to manully select pixels of an image. After selecting pixels, the a list of RGB values for the selected pixels is displayed to the user. The RGB values were imported into EXCEL and the maximum and minimum values were calculated for each channel (R, G, and B). This process was carried out for a bright and dark image.

