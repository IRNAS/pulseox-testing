import numpy as np


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
