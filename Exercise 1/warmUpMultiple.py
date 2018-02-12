#<!--------------------------------------------------------------------------->
#<!--                   ITU - IT University of Copenhage                    -->
#<!--                      Computer Science Department                      -->
#<!--                    Eye Information Research Group                     -->
#<!--       Introduction to Image Analysis and Machine Learning Course      -->
#<!-- File       : warmUpMatplotlib.py                                      -->
#<!-- Description: Example of code for showing images using Matplotlib      -->
#<!-- Author     : Fabricio Batista Narcizo                                 -->
#<!--            : Rued Langgaards Vej 7 - 4D25 - DK-2300 - Kobenhavn S.    -->
#<!--            : narcizo[at]itu[dot]dk                                    -->
#<!-- Responsable: Dan Witzner Hansen (witzner[at]itu[dot]dk)               -->
#<!--              Fabricio Batista Narcizo (fabn[at]itu[dot]dk)            -->
#<!-- Information: You DO NOT need to change this file                      -->
#<!-- Date       : 19/01/2018                                               -->
#<!-- Change     : 19/01/2018 - Creation of this script                     -->
#<!-- Review     : 19/01/2018 - Finalized                                   -->
#<!--------------------------------------------------------------------------->

__version__ = "$Revision: 2018011901 $"

###############################################################################
import matplotlib
matplotlib.use("tkagg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

###############################################################################

# Vector to keep the input images
images = []

# Open the images as color images.
images.append(mpimg.imread("./inputs/tinky_winky.jpg"))
images.append(mpimg.imread("./inputs/dipsy.jpg"))
images.append(mpimg.imread("./inputs/laa_laa.jpg"))
images.append(mpimg.imread("./inputs/po.jpg"))

# Create the Matplotlib window.
fig = plt.figure("Images")

# Show the input images in a Matplotlib window.
for i, image in zip(range(4), images):
    fig.add_subplot(1, 4, i + 1)
    plt.axis("off")
    plt.imshow(image)

plt.show()

# Create the Matplotlib window.
fig = plt.figure("Matrix")

# Show the input images in a Matplotlib window.
for i, image in zip(range(4), images):
    fig.add_subplot(2, 2, i + 1)
    plt.axis("off")
    plt.imshow(image)

plt.show()