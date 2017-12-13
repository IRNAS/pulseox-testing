# Statistical Trials for Pulse-Oximeter Probe Performance

SQI has to be validated statistically by following the following procedure:

  - Pre-step 1: Have two devices ready, one with 'clean firmware' (device A) and one with 'debug firmware' (device B) flashed on them.
  - Pre-step 2: Connect the UART bridge to the device B so that it is ready to send data to the PC.
  - Pre-step 3: Get the finger clip ready and instruct the volunteer to rest their arm on the table and not move during the measurement. 
  
  
  ## TEST A
  Plug the finger probe into device A. Instruct the patient to mount the finger clip on their index finger in any orientation.
  
  Requirements: 
  - the device must run flawlessly showing both SpO2% and HR values for at least 30s. 
  - the device must stop showing values once the finger clip is dismounted
  - the device must begin showing values on the display after the finger clip has been mounted again after maximum 10s.
 
 If all three requirements are satisfied, continue with TEST B.
 
  ## TEST B
 Plug the finger clip into device B. Instruct the patient to mount the finger clip on to their index finger in 'UP' orientation. 
 
 Capture the data of at least 1min. Perform this test on index finger and little finger, in both orientations (4 measurements all together).
 
 Orientation legend is as follows:
 
 ||LED|SENSOR|
 |------|--------|--------|
 |UP|tip|nail|
 |DOWN|nail|tip|
   
Run the SQI_stats.py code to perform SQI analysis. 

## Device Classification
Since the device is medium-risk (Class II FDA) we need at least 95% confidence interval and 95% reliability therefore the minimum number of samples is 59 for zero defect sampling, 93 for 1 defect sampling and 124 for 2 defect sampling.

References:
  - [Tony Gojanovic: Zero Defect Sampling (2007)](http://asq.org/quality-progress/2007/11/basic-quality/zero-defect-sampling.html)
  - [Mark Durivage: Sample Sizes: How Many Do I Need? (2014)](https://www.qualitymag.com/articles/91991-sample-sizes-how-many-do-i-need)