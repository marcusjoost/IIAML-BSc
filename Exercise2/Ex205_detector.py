#<!--------------------------------------------------------------------------->
#<!--                   ITU - IT University of Copenhage                    -->
#<!--                      Computer Science Department                      -->
#<!--                    Eye Information Research Group                     -->
#<!--       Introduction to Image Analysis and Machine Learning Course      -->
#<!-- File       : Ex205_detector.py                                        -->
#<!-- Description: Script to detect objects based on colors in some image   -->
#<!--            : sequences from a video file or a webcam                  -->
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
import numpy as np

########################################################################
# Construct the argument parse and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="Path to the (optional) video file")
args = vars(ap.parse_args())

# Load a video camera or a video file.
if not args.get("video", False):
    video = cv2.VideoCapture(0)
else:
    video = cv2.VideoCapture(args["video"])

# Grab each individual frame.
while True:
    # Grabs, decodes and returns the next video frame.
    retval, frame = video.read()

    # Check if there is a valid frame.
    if not retval:
        break

    #<!--------------------------------------------------------------------------->
    #<!--                            YOUR CODE HERE                             -->
    #<!--------------------------------------------------------------------------->
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame,frame, mask= mask)
 

    # Remove this line after you finish the exercise.

    #<!--------------------------------------------------------------------------->
    #<!--                                                                       -->
    #<!--------------------------------------------------------------------------->

    # Show the processed images.
    cv2.imshow("Result", result)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    
    # Get the keyboard event.
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Closes video file or capturing device.
video.release()

# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
