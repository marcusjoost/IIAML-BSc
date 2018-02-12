#<!--------------------------------------------------------------------------->
#<!--                   ITU - IT University of Copenhage                    -->
#<!--                      Computer Science Department                      -->
#<!--                    Eye Information Research Group                     -->
#<!--       Introduction to Image Analysis and Machine Learning Course      -->
#<!-- File       : Ex305_linear_algebra.py                                  -->
#<!-- Description: Script to solve linear equation systems                  -->
#<!-- Author     : Fabricio Batista Narcizo                                 -->
#<!--            : Rued Langgaards Vej 7 - 4D25 - DK-2300 - Kobenhavn S.    -->
#<!--            : narcizo[at]itu[dot]dk                                    -->
#<!-- Responsable: Dan Witzner Hansen (witzner[at]itu[dot]dk)               -->
#<!--              Fabricio Batista Narcizo (fabn[at]itu[dot]dk)            -->
#<!-- Information: You DO NOT need to change this file                      -->
#<!-- Date       : 06/02/2018                                               -->
#<!-- Change     : 06/02/2018 - Creation of this script                     -->
#<!-- Review     : 06/02/2018 - Finalized                                   -->
#<!--------------------------------------------------------------------------->

__version__ = "$Revision: 2018020601 $"


########################################################################
import matplotlib.pyplot as plt
import numpy as np

########################################################################

# This function creates a Matplotlib window and shows four histograms.
def showData(data, marker="x", color="black", title="World Population in Billions"):
    plt.title(title)
    plt.xlim([1950, 2005])
    plt.xlabel("Year")
    plt.ylabel("Population in Billions")
    plt.scatter(data[:, 0], data[:, 1], marker=marker, color=color)
    
#<!--------------------------------------------------------------------------->
#<!--                            YOUR CODE HERE                             -->
#<!--------------------------------------------------------------------------->



#<!--------------------------------------------------------------------------->
#<!--                                                                       -->
#<!--------------------------------------------------------------------------->

# Open the data set and create X, y and m variables.
# X: years.
# y: population in bilions.
filename = "inputs/data.txt"
data = np.loadtxt(filename, delimiter=",")
X = np.array([data[:, 0]]).T
y = np.array([data[:, 1]]).T
m = len(y)

# Plot the training dataset.
plt.figure("Input Data")
showData(data)
plt.show()

# Create a column of ones.
ones = np.ones((m, 1))

#<!--------------------------------------------------------------------------->
#<!--                            YOUR CODE HERE                             -->
#<!--------------------------------------------------------------------------->



#<!--------------------------------------------------------------------------->
#<!--                                                                       -->
#<!--------------------------------------------------------------------------->
