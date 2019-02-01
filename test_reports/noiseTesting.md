# Noise Testing

## Introduction
It was found during performance testing that Glia pulse oximeter V2.2 fails at low amplitude signals due to masking. The useful signal is masked by noise which results in failure of peak/trough recognition. Trough recognition is the baseline for further signal processing in the device. Therefore, the device has been split into segments on which noise testing will be performed in order to investigate the noise sources.

DIAGRAM

## Light Receiver Noise Test

Date of testing: 31 Jan 2019

Test setup: TSL251 light-to voltage converter has been isolated from pulse oximeter. It was powered up directly from a DC power supply and output was connected to the oscilloscope. Noise level was analysed at different mean signal levels.


