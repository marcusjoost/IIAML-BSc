#<!--------------------------------------------------------------------------->
#<!--                   ITU - IT University of Copenhage                    -->
#<!--                      Computer Science Department                      -->
#<!--                    Eye Information Research Group                     -->
#<!--       Introduction to Image Analysis and Machine Learning Course      -->
#<!-- File       : Ex203_histogram.py                                       -->
#<!-- Description: Script to represent the pixel distribution function      -->
#<!--            : based on each grayscale level of an input image          -->
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
filename = "./inputs/lena.jpg" if args["image"] is None else args["image"]

# Loads a grayscale image from a file passed as argument.
image = cv2.imread(filename, cv2.IMREAD_COLOR)

# Create the Matplotlib figures.
fig_imgs = plt.figure("Images")
fig_hist = plt.figure("Histograms")

# This function creates a Matplotlib window and shows four images.
def showImage(image, pos, title="Image", isGray=False):
    sub = fig_imgs.add_subplot(2, 2, pos)
    sub.set_title(title)
    if isGray:
        sub.imshow(image, cmap="gray")
    else:
        sub.imshow(image)
    sub.axis("off")

# This function creates a Matplotlib window and shows four histograms.
def showHistogram(histogram, pos, title="Histogram"):
    sub = fig_hist.add_subplot(2, 2, pos)
    sub.set_title(title)
    plt.xlabel("Bins")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.plot(histogram)

#<!--------------------------------------------------------------------------->
#<!--                            YOUR CODE HERE                             -->
#<!--------------------------------------------------------------------------->
his1 = cv2.calcHist([image],[0],None,[256],[0,256])
showHistogram(his1,1)
showImage(image, 1)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(image_rgb)

img3 = cv2.merge([b,g,r])
his3 = cv2.calcHist([img3],[0],None,[256],[0,256])

showHistogram(his3,2)
showImage(img3, 2)
#img2 = np.zeros((image.shape), dtype='int32')
#img2 += image
#img2 = np.random.shuffle(img2)
#his2 = cv2.calcHist([img2],[0],None,[256],[0,256])
#showHistogram(his2,2)
#showImage(img2,2)
#<!--------------------------------------------------------------------------->
#<!--                                                                       -->
#<!--------------------------------------------------------------------------->

# Show the Matplotlib windows.
plt.show()
