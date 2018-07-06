# -*- coding: utf-8 -*-
"""
Created on 2017 Nov 19 

@ author: Luka Banovic
@ email: banovic@irnas.eu


BUTTRTWORTH RED ADDED
"""


import os
os.chdir(r'/home/irnas/Documents/GliaX/pulseoxi/V2-2')			# insert the path to working directory
import pandas
import numpy as np
from scipy.signal import butter, filtfilt
import matplotlib.pyplot as plt


def load_dataset(filename):
    """
	This function reads the data from a .txt file.
    """
    data = pandas.read_csv(filename, header=None, names=['ts', 'raw_ir', 'dc_ir', 'mean_ir', 'butt_ir', 'dc_red', 'butt_red', 'raw_orange','raw_yellow','norm_ir','norm_red','butt_norm_ir','butt_norm_red','ratio','ambient','raw_red'])
    time = data['ts']
    time = data['ts'] - data['ts'][0]
    time = time/1000

    raw_ir = data['raw_ir']
    dc_ir = data['dc_ir']/100
    mean_ir = data['mean_ir']/100
    butt_ir = data['butt_ir']/100
    dc_red = data['dc_red']/100
    butt_red = data['butt_red']/100
    raw_orange = data['raw_orange']
    raw_yellow = data['raw_yellow']
    norm_red = data['norm_red']/100000
    norm_ir = data['norm_ir']/100000
    b_n_red = data['butt_norm_red']/100000
    b_n_ir = data['butt_norm_ir']/100000
    ratio = data['ratio']/100
    ambient = data['ambient']
    raw_red = data['raw_red']
    return time, raw_ir, dc_ir, mean_ir, butt_ir, dc_red, butt_red, raw_orange, raw_yellow, norm_red, norm_ir, b_n_red, b_n_ir, ratio, ambient, raw_red
        
    
def butter_lowpass(cut, fs, order=2):
    nyq = 0.5 * fs
    cut = cut / nyq
    b, a = butter(order, [cut], btype='low')
    return b, a

def butter_lowpass_filter(data, cut, fs, order=2):
    b, a = butter_lowpass(cut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

def butter_highpass(cut, fs, order=2):
    nyq = 0.5 * fs
    cut = cut / nyq
    b, a = butter(order, [cut], btype='high')
    return b, a

def butter_highpass_filter(data, cut, fs, order=2):
    b, a = butter_highpass(cut, fs, order=order)
    y = filtfilt(b, a, data)
    return y


class PeakDetector(object):
    def __init__(self, threshold):
        self.threshold = threshold
        self.previous_value = None
        self.state = 'idle'

    def push(self, value):
        if self.state == 'idle':
            if value <= self.threshold:
                self.state = 'rising'
        
        elif self.state == 'rising':
            if value < self.previous_value:
                pass
            else:
                self.state = 'falling'
                return True
        elif self.state == 'falling':
            if value > self.threshold:
                self.state = 'idle'

        self.previous_value = value
        return False    


def trough_decection(signal, treshold):
    """
    """
    detector = PeakDetector(threshold=treshold)
    peaks = [detector.push(x) for x in signal]
    peaks = np.asarray(peaks)
    
    item = True
    peaks = np.where(peaks == item)
    peaks = peaks[0]
    return peaks

"""======================================================================="""   


def get_p2p_amp(signal, locs):
    """
	signal = Low-Pass filtered DC signal
    """
    max_p2p_mean = np.mean(np.abs(signal[locs]))
    amp = 2*max_p2p_mean
    
    return amp

def SQI( signal, noise, locs):
    """
	signal = clean signal - DC-filtered and Low-Pass filtered below 3.3Hz
	noise = raw signal DC-filtered and High-Pass filtered above 3.3Hz
	locs = trough locations [trough_decection(signal, treshold=0)]
    """
    STD = np.sqrt(np.var(noise))		# noise standard deviation
    AMP = get_p2p_amp(signal, locs)		# signal amplitude
    
    SQI = 1 - STD/AMP
    
    return SQI, AMP, STD

"""======================================================================="""   
filename = 'silicone_thin_adapt.txt'
time, raw_ir, dc_ir, _, butt_ir, dc_red, butt_red, _, _, _, _, _, _, _, _, raw_red = load_dataset(filename)

ir_noise = butter_highpass_filter(raw_ir, 3.3, 100, order=2)
red_noise = butter_highpass_filter(raw_red, 3.3, 100, order=2)

peaks = trough_decection(butt_ir, treshold=0)

buffer_start = peaks[int(np.floor(len(peaks))/2)-3]
buffer_end = peaks[int(np.floor(len(peaks))/2)+3]

sqi_peaks = peaks[int(np.floor(len(peaks))/2)-3:int(np.floor(len(peaks))/2)+3]

sqi_ir, amp_ir, std_ir = SQI(butt_ir[buffer_start:buffer_end], ir_noise[buffer_start:buffer_end], sqi_peaks)
sqi_red, amp_red, std_red = SQI(butt_red[buffer_start:buffer_end], red_noise[buffer_start:buffer_end], sqi_peaks)


plt.plot(time, raw_ir)
plt.plot(time, raw_red)