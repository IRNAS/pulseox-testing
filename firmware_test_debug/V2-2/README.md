In this folder you can find test and clean firmware of device V2-2.

**TEST FIRMWARE**

FILE: `test_V2-2.bin`
 
Test firmware is used to optimize calibration parameters such that the device reaches steady state in the shortest possible time interval. 
  
  1. Flash test firmware onto Glia Pulse Oximeter as instructed [here](https://github.com/IRNAS/pulseox-testing/blob/master/01_firmware_flashing_instructions.md)
  
  2. Unplug the programmer board and reset the pulse oximeter by turning it OFF and ON again
  
  3. The display will show "FINGER OUT" sign until patient's finger is inserted. Once finger is inserted "CALIBRATING..." sign will show up. The calibration is now initialized.
  
  3. Once the calibration is complete, the values on the screen will show up showing the optimal IR brightness level, RED brightness level and DURATION of calibration. 
  
  4. Log all values in `brightness_test_log.ods` file, including description of conditions (skin color, age, finger thickness etc.).
  
  The current firmware will be adjusted at the next stage based on these logged values and final functional release will be made.
  
 **CLEAN FIRMWARE**
 
 FILE: `clean_V2-2.bin`
 
 Clean firmware allows normal device operation. Currently, default initial brightness levels are implemented, therefore potential delay of procedure can be expected under certain conditions (thinner fingers, darker skin color etc.) due to longer calibration time. Upon completion of the procedure described above, this risk can be addressed and reduced by optimization of initial parameters.
  
