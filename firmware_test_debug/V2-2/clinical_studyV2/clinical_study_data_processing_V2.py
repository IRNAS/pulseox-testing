"""
Created on 2019 Feb 10 

@ author: Luka Banovic
@ email: banovic@irnas.eu


This script enables you to process the logged data from your Glia pulse oximeter. It must be saved in the same directory as the recorded .txt files.

A series of values in one row are:
  
  - timestamp ('ts')
  - ratio between IR and red ('ratio')

"""

import numpy as np
import matplotlib.pyplot as plt


def load_dataset(filename):
    """
	This function reads the data from a .txt file.

	:param: filename - str() - name of the .txt file where data are recorded (must include '.txt' at the end).

	:output: time vector and ratio vector
    """
    data = np.genfromtxt(filename, delimiter=',', skip_header=1, dtype='float')		# read the file

    time = data[:,0]		# time data
    rawIR = data[:,1]       # raw ir
    buttIR = data[:,2]      # butt_ir
    buttRed = data[:,3]     
    ratio = data[:,4]		# ratio data
    rawRed = data[:,5]
    sqiIR = data[:,6]
    sqiRed = data[:,7]

    time = time - time[0]	# subtract the first value from all values such that you start at 0 seconds
    time = time/1000		# convert to seconds

    rawIR = rawIR/100
    buttIR = buttIR/100
    buttRed = buttRed/100
    ratio = ratio/100		# - !! DO NOT REMOVE !! division by 100 due to firmware optimization
    rawRed = rawRed/100
    sqiIR = sqiIR/100
    sqiRed = sqiRed/100

    ratio[ratio == 0.] = 'nan'	# removing all zeros
    ratio[ratio > 2.] = 'nan'	# safety measure: removing the first outlier that occurs due to device stabilization




    return time, rawIR, buttIR, buttRed, ratio, rawRed, sqiIR, sqiRed 

   
if __name__ == "__main__":
	
	"""
	The user must insert the file name (e.g. recording.txt in the string ('') below.
	"""

	filename = 'sample_file.txt'        				# insert the filename
	time, rawIR, buttIR, buttRed, ratio, rawRed, sqiIR, sqiRed = load_dataset(filename)		# load the data

	# plot ratio
	plt.figure(1)					# plot the data
	plt.plot(time, ratio, 'bo')			# limit the axes
	plt.ylim([0, 2])
	plt.xlabel("Time (s)")
	plt.ylabel("Ratio")
	
    # plot butt signals
	plt.figure(2)
	plt.plot(time, buttIR, 'b')
	plt.plot(time, buttRed, 'r')
	plt.xlabel("Time (s)")
	plt.ylabel("buttIR/buttRed")
	plt.legend(["IR","RED"])
	plt.ylim([-40,20])
	plt.show()


