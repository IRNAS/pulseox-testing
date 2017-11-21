# -*- coding: utf-8 -*-
"""
Created on 2017 Nov 19 

@ author: Luka Banovic
@ email: banovic@irnas.eu



"""


import os
os.chdir(r'......')     # insert working directory


import pandas
import numpy as np
from scipy.signal import butter, filtfilt, welch
from scipy import integrate
import glob
import matplotlib.pyplot as plt


def load_dataset_2(filename):
    """
    This function reads the .txt file and outputs all data series as variables.
    """
    data = pandas.read_csv(filename, header=None, names=['ts', 'raw_ir', 'dc_ir', 'mean_ir', 'butt_ir', 'dc_red','raw_orange','raw_yellow','norm_ir','norm_red','butt_norm_ir','butt_norm_red','ratio','ambient'])
    time = data['ts']
    time = data['ts'] - data['ts'][0]
    time = time/100

    raw_ir = data['raw_ir']
    dc_ir = data['dc_ir']
    mean_ir = data['mean_ir']
    butt_ir = data['butt_ir']
    dc_red = data['dc_red']
    raw_orange = data['raw_orange']
    raw_yellow = data['raw_yellow']
    norm_red = data['norm_red']
    norm_ir = data['norm_ir']
    b_n_red = data['butt_norm_red']
    b_n_ir = data['butt_norm_ir']
    ratio = data['ratio']
    return time, raw_ir, dc_ir, mean_ir, butt_ir, dc_red, raw_orange, raw_yellow, norm_red, norm_ir, b_n_red, b_n_ir, ratio
        
        
def butter_lowpass(cut, fs, order=5):
    nyq = 0.5 * fs
    cut = cut / nyq
    b, a = butter(order, [cut], btype='low')
    return b, a

def butter_lowpass_filter(data, cut, fs, order=5):
    b, a = butter_lowpass(cut, fs, order=order)
    y = filtfilt(b, a, data)
    return y

def butter_highpass(cut, fs, order=5):
    nyq = 0.5 * fs
    cut = cut / nyq
    b, a = butter(order, [cut], btype='high')
    return b, a

def butter_highpass_filter(data, cut, fs, order=5):
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

def SQI( signal, break_frequency):
    """
    """

    # PSD calculation
    freqs, p_signal = welch(signal, fs=100)

    # normalization       
    p_signal = p_signal/max(p_signal)

    # break point
    start_point = np.argmax(freqs>break_frequency)

    # frequency step for integration
    dx = freqs[1]
    
    # integration
    int_sig = integrate.trapz(p_signal[:start_point], dx=dx)
    int_total = integrate.trapz(p_signal, dx=dx)
    
    # index calculation
    
        
    
    SQI = int_sig/int_total
    

    return SQI
    
def check_index(index, lower, upper):
        
    if index > upper or index < lower:
        warning_int = 1
        
    else:
        warning_int=0
    return warning_int


"""======================================================================="""
if __name__=='__main__':
    
    index_red = []  # empty list of indeces for RED signal
    index_ir = []   # empty list of indeces for IR signal
    warning_msgs = []
#    
    # get a list of all filenames in the directory    
    directory = glob.glob('*.txt')


    for filename in directory:
        # data load in            
        time, raw_ir, dc_ir, _, _, dc_red, _, _, _, _, _, _, _ = load_dataset_2(filename)
            
        # low pass filters
        dc_ir_ftd = butter_lowpass_filter(dc_ir, 3.3, 100, order=2)
    
        #trough detection
        peaks = trough_decection(dc_ir_ftd, treshold=0)
        
        #glia index
        red_index = SQI(dc_red, 3.3)
        index_red.append(round(red_index,2))
        warn_red = check_index(red_index, 0.3, 0.85)    # check warning range
           
        ir_index = SQI(dc_ir, 3.3)
        index_ir.append(round(ir_index,2))
        warn_ir = check_index(ir_index, 0.2, 0.95)      # check warning range
        
        
        
        if warn_ir and warn_red == 1:
            warning_msgs.append('CHECK BOTH')
        elif warn_ir == 1:
            warning_msgs.append('CHECK IR')
        elif warn_red == 1:
            warning_msgs.append('CHECK RED')
        else:
            warning_msgs.append('---')
    
        
    d = {'filename': directory, 'IR': index_ir, 'RED': index_red, 'WARNINGS': warning_msgs}
    print(pandas.DataFrame(data=d))