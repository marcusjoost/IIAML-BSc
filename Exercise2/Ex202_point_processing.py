#<!--------------------------------------------------------------------------->
#<!--                   ITU - IT University of Copenhage                    -->
#<!--                      Computer Science Department                      -->
#<!--                    Eye Information Research Group                     -->
#<!--       Introduction to Image Analysis and Machine Learning Course      -->
#<!-- File       : Ex202_point_processing.py                                -->
#<!-- Description: Script to apply a transformation in a pixel of f(x, y)   -->
#<!--            : input image to a pixels in g(x, y) output image          -->
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
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# Create a Matplotlib window.
fig = plt.figure()

# Global variables used for point processing.
# a: parameter used for changing contrast.
# b: parameter used for changing brightness.
# c: paramater used for changing negative.
a = 1.
b = 0.
c = 0.

# This function updates the transformed image and the plots.
def update():
    # This vector contains a list of all valid grayscale level.
    bins = np.array(range(256))
    
    # Call here the transformation function.
    g = pointProcessing(image, a, b, c)
    
    # Display the resulting image.
    cv2.imshow("Point Processing", g)

    # Clear the plot before showing the new function.
    if (len(sub1.lines)):
        sub1.lines.pop()
    if (len(sub2.lines)):
        sub2.lines.pop()
    if (len(sub3.lines)):
        sub3.lines.pop()
    if (len(sub4.lines)):
        sub4.lines.pop()

    # Contrast changes.
    result = contrast(bins, a)
    sub1.plot(bins, result, "r-", linewidth=5)

    # Bightness changes.
    result = brightness(bins, b)
    sub2.plot(bins, result, "g-", linewidth=5)

    # Negative changes.
    result = negative(bins, c)
    sub3.plot(bins, result, "b-", linewidth=5)

    # Point Processing changes.
    result = pointProcessing(bins, a, b, c)
    sub4.plot(bins, result, "k-", linewidth=5)    

    # Show the updated window.
    plt.show()

# This function will be performed when the user change the contrast value.
def changeA(value):
    # Global variable: include the contrast transformation on a.
    global a

    a = value * 0.1
    #<!--------------------------------------------------------------------------->
    #<!--                            YOUR CODE HERE                             -->
    #<!--------------------------------------------------------------------------->



    #<!--------------------------------------------------------------------------->
    #<!--                                                                       -->
    #<!--------------------------------------------------------------------------->

    # Update the transformed image.
    update()

# This function will be performed when the user change the brightness value.
def changeB(value):
    # Global variable: include the brightness transformation on b.
    global b
    
    b = value - 128
    #<!--------------------------------------------------------------------------->
    #<!--                            YOUR CODE HERE                             -->
    #<!--------------------------------------------------------------------------->



    #<!--------------------------------------------------------------------------->
    #<!--                                                                       -->
    #<!--------------------------------------------------------------------------->

    # Update the transformed image.
    update()

# This function will be performed when the user change the negative value.
def changeC(value):
    # Global variable: include the negative transformation on c.
    global c

    c = 255 * value
    #<!--------------------------------------------------------------------------->
    #<!--                            YOUR CODE HERE                             -->
    #<!--------------------------------------------------------------------------->



    #<!--------------------------------------------------------------------------->
    #<!--                                                                       -->
    #<!--------------------------------------------------------------------------->

    # Update the transformed image.
    update()

def contrast(f, a):
    #<!--------------------------------------------------------------------------->
    #<!--                            YOUR CODE HERE                             -->
    #<!--------------------------------------------------------------------------->
    f = a * f
    f[f > 255] = 255
    f = f.astype('uint8')
    # Remove this command.
    return f

    #<!--------------------------------------------------------------------------->
    #<!--                                                                       -->
    #<!--------------------------------------------------------------------------->

def brightness(f, b):
    #<!--------------------------------------------------------------------------->
    #<!--                            YOUR CODE HERE                             -->
    #<!--------------------------------------------------------------------------->
    g = np.zeros((f.shape), dtype='uint16')
    g = g + f + b

    g[g > 255] = 255
    g[g < 0] = 0
    #np.clip(f, 0, 255)
    g = g.astype('uint8')
    # Remove this command.
    return g

    #<!--------------------------------------------------------------------------->
    #<!--                                                                       -->
    #<!--------------------------------------------------------------------------->

def negative(f, c):
    #<!--------------------------------------------------------------------------->
    #<!--                            YOUR CODE HERE                             -->
    #<!--------------------------------------------------------------------------->
    g = np.zeros((f.shape), dtype='int16')
    g = np.abs((f + g) - c)
    g = g.astype('uint8')
    # Remove this command.
    return g

    #<!--------------------------------------------------------------------------->
    #<!--                                                                       -->
    #<!--------------------------------------------------------------------------->

def pointProcessing(f, a, b, c):
    #g = contrast(f, a)
    #g = brightness(g, b)
    #g = negative(g, c)
    g = np.zeros((f.shape), dtype='int16')
    g = f + g
    g = np.abs((a * f + b) - c)
    g[g > 255] = 255
    #g[g < 0] = 0
    #np.clip(f, 0, 255)

    g = g.astype('uint8')
    return g

# Contrast graphic.
sub1 = fig.add_subplot(2, 2, 1)
sub1.set_title("Contrast")
plt.axis([0, 255, 0, 255])
plt.grid(None, 'major', 'both')

# Brightness graphic.
sub2 = fig.add_subplot(2, 2, 2)
sub2.set_title("Brightness")
plt.axis([0, 255, 0, 255])
plt.grid(None, 'major', 'both')

# Negative graphic.
sub3 = fig.add_subplot(2, 2, 3)
sub3.set_title("Negative")
plt.axis([0, 255, 0, 255])
plt.grid(None, 'major', 'both')

# Point processing graphic.
sub4 = fig.add_subplot(2, 2, 4)
sub4.set_title("Point Processing")
plt.axis([0, 255, 0, 255])
plt.grid(None, 'major', 'both')

# Creates an OpenCV window with three trackbars.
cv2.namedWindow("Point Processing")
cv2.createTrackbar("Contrast",   "Point Processing",  10,  20, changeA)
cv2.createTrackbar("Brightness", "Point Processing", 128, 256, changeB)
cv2.createTrackbar("Negative",   "Point Processing",   0,   1, changeC)

# Show the input image and the graphics.
update()

cv2.waitKey(0)

# Show the plots window.
plt.show()

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
