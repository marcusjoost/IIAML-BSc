#<!--------------------------------------------------------------------------->
#<!--                   ITU - IT University of Copenhage                    -->
#<!--                      Computer Science Department                      -->
#<!--                    Eye Information Research Group                     -->
#<!--       Introduction to Image Analysis and Machine Learning Course      -->
#<!-- File       : warmUpImage.py                                           -->
#<!-- Description: Example of code for opening images using OpenCV          -->
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

###############################################################################

# Full path where is located the input image.
filepath = "./inputs/lena.jpg"

# Open the image as a color image.
image = cv2.imread(filepath)

# Show the input image in a OpenCV window.
cv2.imshow("Image", image)
cv2.waitKey(0)

# When everything done, release the OpenCV window.
cv2.destroyAllWindows()