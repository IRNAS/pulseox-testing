In this folder you can find debug and clean [firmware of device V2-2](https://github.com/IRNAS/pulseox-firmware/tree/V2-2).

**DEBUG FIRMWARE**

FILE: ```debug_V2-2.bin``` 

Debug firmware allows to transmit all variables onto the PC and inspect them (as described [here](https://github.com/IRNAS/pulseox-testing/blob/master/03_debugging.md)).
  
 **CLEAN FIRMWARE**
 
 FILE: `clean_V2-2.bin`
 
 Clean firmware allows normal device operation. 
 
 Disclaimer: Currently, default initial brightness levels are implemented, therefore potential delay of procedure can be expected under certain conditions (thinner fingers, darker skin color etc.) due to longer calibration time. Upon completion of the procedure described [in this issue](https://github.com/IRNAS/pulseox-testing/issues/2), this risk can be addressed and reduced by optimization of initial parameters. For this,`test_V2-2.bin` should be used.
