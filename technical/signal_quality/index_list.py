import numpy as np
def find_index(clean_signal, std_list):
    """
    This function takes every element i from the list of standard deviation values 'std_list' and generates the random noise with the respective standard deviation. The mean and length of the noise signal equal to the ones of the clean signal. The noise is than added to the clean signal and the SQI is calculated.
    
    The function returns the list of SQIs at each i.
    
    Created on 2017 Nov 19 

@ author: Luka Banovic
@ email: banovic@irnas.eu
    """
    index_list = []
    for i in std_list:
        noise = generate_noise(np.mean(clean_signal), i, len(clean_signal))
        build = noise + clean_signal
        index_list.append(SQI(build,3.3))
    
    return index_list
