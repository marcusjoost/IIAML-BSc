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
import cv2
import matplotlib
matplotlib.use("tkagg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

###############################################################################

# Full path where is located the input image.
filepath = "./inputs/black.jpg"

# Open the image as a grayscale image.
image1 = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
print("Width: %d pixels." % (image1.shape[1]))
print("Height: %d pixels." % (image1.shape[0]))

# Open the image using Matplotlib.
image2 = mpimg.imread(filepath)
image2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)

# Create the Matplotlib window.
plt.figure("Matplotlib")

# Create the OpenCV window.
cv2.namedWindow("OpenCV", cv2.WINDOW_AUTOSIZE)

# Show the input image in a OpenCV window.
cv2.imshow("OpenCV", image1)

# Show the input image in a Matplotlib window.
imgplot = plt.imshow(image2)
plt.show()

# When everything done, release the OpenCV window.
cv2.destroyAllWindows()
