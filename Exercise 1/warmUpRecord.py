#<!--------------------------------------------------------------------------->
#<!--                   ITU - IT University of Copenhage                    -->
#<!--                      Computer Science Department                      -->
#<!--                    Eye Information Research Group                     -->
#<!--       Introduction to Image Analysis and Machine Learning Course      -->
#<!-- File       : warmUpCapture.py                                         -->
#<!-- Description: Example of code for recording videos using OpenCV        -->
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
import time

###############################################################################

# Create a capture video object.
capture = cv2.VideoCapture(0)

# Get the video resolution.
w = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = round(capture.get(cv2.CAP_PROP_FPS))

# Check if the fps variable has a correct value.
fps = fps if fps > 0 else 30

# Create a record video object.
isColor = False
fourcc  = cv2.VideoWriter_fourcc(*"mp4v")
record  = cv2.VideoWriter("outputs/warmUpVideo.mov",
                          fourcc, fps, (w, h), isColor)

# Create an OpenCV window.
cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)

# This repetion will run while there is a new frame in the video file or
# while the user do not press the "q" (quit) keyboard button.
while True:
    # Capture frame-by-frame.
    retval, frame = capture.read()

    # Check if there is a valid frame.
    if not retval:
        break

    # Convert the input image to grayscale.
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    record.write(grayscale)

    # Resize the input image.
    image = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Display the resulting frame.
    cv2.imshow("Image", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture and record objects.
record.release()
capture.release()
cv2.destroyAllWindows()
