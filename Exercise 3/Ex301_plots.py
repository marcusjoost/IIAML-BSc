#]<!--------------------------------------------------------------------------->
#<!--                   ITU - IT University of Copenhage                    -->
#<!--                      Computer Science Department                      -->
#<!--                    Eye Information Research Group                     -->
#<!--       Introduction to Image Analysis and Machine Learning Course      -->
#<!-- File       : Ex301_plots.py                                           -->
#<!-- Description: Script to load data and plot lines and scatters          -->
#<!--            : sequences from a video file or a webcam                  -->
#<!-- Author     : Fabricio Batista Narcizo                                 -->
#<!--            : Rued Langgaards Vej 7 - 4D25 - DK-2300 - Kobenhavn S.    -->
#<!--            : narcizo[at]itu[dot]dk                                    -->
#<!-- Responsable: Dan Witzner Hansen (witzner[at]itu[dot]dk)               -->
#<!--              Fabricio Batista Narcizo (fabn[at]itu[dot]dk)            -->
#<!-- Information: You DO NOT need to change this file                      -->
#<!-- Date       : 05/02/2018                                               -->
#<!-- Change     : 05/02/2018 - Creation of this script                     -->
#<!-- Review     : 05/02/2018 - Finalized                                   -->
#<!--------------------------------------------------------------------------->

__version__ = "$Revision: 2018020501 $"

########################################################################
import matplotlib.pyplot as plt
import numpy as np

########################################################################

#<!--------------------------------------------------------------------------->
#<!--                            YOUR CODE HERE                             -->
#<!--------------------------------------------------------------------------->

array_01 = [1,5,9]
array_02 = [4,8,16,32,64,128]
array_03 = [7,8,9,10,11,12]
array_04 = np.array(np.linspace(2,50,10))

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax1.plot(array_01,"g")

ax2 = fig.add_subplot(222)
ax2.scatter(array_03, array_02, 10, color='red')

sigmoid = lambda x: 1/ (1 + np.exp(-x))

ax3 = fig.add_subplot(223)
ax3.plot(sigmoid(array_04))

#plt.tight_layout()
#fig = plt.gcf()
fig.show()

#<!--------------------------------------------------------------------------->
#<!--                                                                       -->
#<!--------------------------------------------------------------------------->
plt.show()
