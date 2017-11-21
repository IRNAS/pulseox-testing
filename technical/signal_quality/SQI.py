import numpy as np
from scipy.signal import welch
from scipy import integrate

def SQI( signal, break_frequency):
    """
    This function calculates the power spectral density of the 'signal' and calulates the ratio of the signal energy below the 'break_frequency' against the total signal energy. 
    
    Created on 2017 Nov 19 

  @ author: Luka Banovic
  @ email: banovic@irnas.eu
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
