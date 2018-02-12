#<!--------------------------------------------------------------------------->
#<!--                   ITU - IT University of Copenhage                    -->
#<!--                      Computer Science Department                      -->
#<!--                    Eye Information Research Group                     -->
#<!--       Introduction to Image Analysis and Machine Learning Course      -->
#<!-- File       : Ex201_color_spaces.py                                    -->
#<!-- Description: Script to convert the input images in two different      -->
#<!--            : color spaces (RGB and HSV)                               -->
#<!-- Author     : Fabricio Batista Narcizo                                 -->
#<!--            : Rued Langgaards Vej 7 - 4D25 - DK-2300 - Kobenhavn S.    -->
#<!--            : narcizo[at]itu[dot]dk                                    -->
#<!-- Responsable: Dan Witzner Hansen (witzner[at]itu[dot]dk)               -->
#<!--              Fabricio Batista Narcizo (fabn[at]itu[dot]dk)            -->
#<!-- Information: You DO NOT need to change this file                      -->
#<!-- Date       : 02/02/2018                                               -->
#<!-- Change     : 02/02/2018 - Creation of this script                     -->
#<!-- Review     : 02/02/2018 - Finalized                                   -->
#<!--------------------------------------------------------------------------->

__version__ = "$Revision: 2018020201 $"

########################################################################
import numpy as np
import argparse
import cv2

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

########################################################################
# Construct the argument parser and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, help="Path to the image")
args = vars(ap.parse_args())

# Create the Matplotlib window.
fig = plt.figure()

# Get the input filename
filename = "./inputs/lena.jpg" if args["image"] is None else args["image"]

# Tips: You can find more information about opening, converting and showing
#       images using OpenCV on warmUpImage.py, warmUpGrayscale.py and
#       warmUpConvert.py Python scripts from the Exercises #01.

image = cv2.imread(filename)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

channel_r, channel_g, channel_b = cv2.split(image_rgb)

height, weidth, channels = image.shape
single =  np.zeros((height, weidth), dtype=np.uint8)

b = cv2.merge([channel_b, single, single])
g = cv2.merge([single, channel_g, single])
r = cv2.merge([single, single, channel_r])

cv2.imshow("red", r)
cv2.imshow("g", g)
cv2.imshow("b", b)


#cv2.imshow("rgb", image_rgb)
#cv2.imshow("hsv", image_hsv)

#channel_r = image_rgb[:, :, 0]
#channel_g = image_rgb[:, 0, :]
#channel_b = image_rgb[0, :, :]
#cv2.imshow("r", channel_r)
#cv2.imshow("g", channel_g)
#cv2.imshow("b", channel_b)

cv2.waitKey(0)

# Show the final image.
plt.show()
