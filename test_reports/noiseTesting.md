# Noise Testing

## Introduction
It was found during performance testing that Glia pulse oximeter V2.2 fails at low amplitude signals due to masking. The useful signal is masked by noise which results in failure of peak/trough recognition. Trough recognition is the baseline for further signal processing in the device. Therefore, the device has been split into segments on which noise testing will be performed in order to investigate the noise sources.

![komplet](https://user-images.githubusercontent.com/14543226/52116790-593dcd00-2612-11e9-827b-da0790edb97f.png)

## Light To Voltage Transmitter (TSL251) Noise Test

Date of testing: 31 Jan 2019

**Test setup:** TSL251 light-to voltage converter has been isolated from pulse oximeter. It was powered up directly from a DC power supply and output was connected to the oscilloscope. Signal variance (peak-to-peak voltage value) was analysed at different mean signal levels. The test was then repeated in an unisolated mode where light-to voltage converter has been powered through the 3V power output from pulse oximeter device.

![isolated 1](https://user-images.githubusercontent.com/14543226/52116979-db2df600-2612-11e9-892e-f037597235e5.png)
![unisolated](https://user-images.githubusercontent.com/14543226/52118161-e33b6500-2615-11e9-8549-26c9de02fcde.png)

The test were performed in a room with white colored walls and fluorescent lighting to simulate hospital room conditions. The sensor output range is between 0V and 2.65V. Mean level was decreased stepwise by shading the sensor with a piece of plastic.

**Results**

Fluorescent lighting noise resulted in low frequency sinusoidal ambient light pulsation.

GRAPH - fluorescent light

Only the thermal noise

**Outcome** of the test was that TSL251 has 200mV peak-to-peak noise level throughout the working range.

