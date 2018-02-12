#<!--------------------------------------------------------------------------->
#<!--                   ITU - IT University of Copenhage                    -->
#<!--                      Computer Science Department                      -->
#<!--                    Eye Information Research Group                     -->
#<!--       Introduction to Image Analysis and Machine Learning Course      -->
#<!-- File       : Ex204_masking.py                                         -->
#<!-- Description: Script to select a specific region in the input image    -->
#<!--            : using a binary mask                                      -->
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
import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np

########################################################################
# Construct the argument parser and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, help="Path to the image")
args = vars(ap.parse_args())

# Get the input filename
filename = "./inputs/zico.jpg" if args["image"] is None else args["image"]

# Loads a grayscale image from a file passed as argument.
image = cv2.imread(filename, cv2.IMREAD_COLOR)

# Create the Matplotlib figure.
fig = plt.figure("Images")

# This function creates a Matplotlib window and shows four images.
def showImage(image, pos, title="Image", isGray=False):
    sub = fig.add_subplot(1, 3, pos)
    sub.set_title(title)
    sub.imshow(image)
    plt.axis("off")
    if isGray:
        sub.imshow(image, cmap="gray")
    else:
        sub.imshow(image)

#<!--------------------------------------------------------------------------->
#<!--                            YOUR CODE HERE                             -->
#<!--------------------------------------------------------------------------->
mask = np.zeros((image.shape[0],image.shape[1]), dtype='uint8')

imgmask1 = cv2.rectangle(mask, (300,300), (500 ,500), (255, 255, 255), -1)
imgmask2 = cv2.circle(mask, (500,500), 100, (255,255,255), -1)
result = cv2.bitwise_and(image, image, mask=imgmask2)
showImage(result, 1)

#<!--------------------------------------------------------------------------->
#<!--                                                                       -->
#<!--------------------------------------------------------------------------->

# Show the Matplotlib windows.
plt.show()
