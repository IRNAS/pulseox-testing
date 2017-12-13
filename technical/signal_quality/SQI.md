# Signal Quality Index

## General
The aim of this algorithm is to quantize the signal quality with a single index (Signal Quality Index - SQI). The future versions of Glia pulse oximeters will have signal quality control implemented in the firmware for more stable performance. 

The SQI is expressed as the **ratio of the signal standard deviation against signal peak-to-peak amplitude.**.

## SQI Range
The SQI range was determined for IR and RED signal separately. It was investigated by extracting the clean signal from the acquired data for which the SQI was obtained. Then, the mean of respective normalized signal (IR or RED) was calculated and used to generate a series of noise signals. 

The random noise began with very small standard deviation (amplitude) and the same mean as the signal had. Then the standard deviation was stepwise increased and the generated noise was added to the clean signal each time and the SQI was calculated. By oberving the amount of false troughs detected we have obtained the SQI range that specifies wether the signal is good enough to be use, or not.
