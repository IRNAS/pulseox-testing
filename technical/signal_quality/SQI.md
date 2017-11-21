# Signal Quality Index

## General
The aim of this algorithm is to quantize the signal quality with a single index (Signal Quality Index - SQI). The future versions of Glia pulse oximeters will have signal quality control implemented in the firmware for more stable performance. 

The SQI is expressed as the **ratio between the energy of the signal up to 3.3Hz and total signal energy**. The energy of the signal is hereby  obtained by integrating the power spectrum in the certain bandwidth.

## SQI Range
The SQI range was determined for IR and RED signal separately. It was investigated by extracting the clean signal from the acquired data for which the SQI was obtained. Then, the standard deviation and mean of respective normalized signal (IR or RED), were calculated and used to generate a series of noise signals. 

The random noise began with very small standard deviation and the same mean as the signal had. Then the standard deviation was stepwise increased and the generated noise was added to the clean signal each time and the SQI was calculated. When the standard deviation of generated noise reached the one of the original signal, the iterations stopped. This way we have obtained the SQI value for a range of standard deviation values. 

**What remains to be done is to verify (using statistics) what's the acceptable range of standard deviation. This piece of information is needed in order to define the acceptable range of SQI.**
