In this folder you can find debug and clean [firmware of device V2-2](https://github.com/IRNAS/pulseox-firmware/tree/V2-2).

**DEBUG FIRMWARE**

FILE: ```debug_V2-2.bin``` 

Debug firmware allows to transmit all variables via UART to the PC and inspect them (instructions can be found [here](https://github.com/IRNAS/pulseox-testing/blob/master/03_debugging.md)). To select which values are desired to be sent out comment or uncomment sections [here](https://github.com/IRNAS/pulseox-firmware/blob/af077f9e98fd172e49468021324ba2b3dae9d09e/src/measurement.c#L648-L702). 

Adapt and run [`04_data_processing.py`](https://github.com/IRNAS/pulseox-testing/blob/master/04_data_processing.py) Python script to visualize data. Make sure to adjust the [respective line](https://github.com/IRNAS/pulseox-testing/blob/0bfbcddb8c8559ee553e9b756a0ef46e382c40d1/04_data_processing.py#L184) such that the readin variables match the sent-out variables.
  
 **CLEAN FIRMWARE**
 
 FILE: `clean_V2-2.bin`
 
 Clean firmware allows normal device operation. 
 
 **DEFAULT BRIGHTNESS VALUES TEST FIRMWARE**
 
Currently, default initial brightness levels are implemented, therefore potential delay of procedure can be expected under certain conditions (thinner fingers, darker skin color etc.) due to longer calibration time. Upon completion of the procedure described [in this issue](https://github.com/IRNAS/pulseox-testing/issues/2), this risk can be addressed and reduced by optimization of initial parameters. For this,`CalibrationTest.bin` test firmware should be used.

**SpO2 CALIBRATION FIRMWARE**

 FILE: `SpO2_calibration.bin`
 
 SpO2 calibration firmware enables calibration of [SpO2 lookup table](https://github.com/IRNAS/pulseox-firmware/blob/f282f3d84f418357f4f4f78a77d248b9474a79d6/src/spo2.h#L25-L30). The instructions for testing can be found  [in this issue](https://github.com/IRNAS/pulseox-testing/issues/3). 
