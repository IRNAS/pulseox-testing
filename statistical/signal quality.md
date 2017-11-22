# Statistical Trials for SQI Investigation

SQI has to be validated statistically by following the following procedure:

  0a. Have two devices ready, one with clean firmware (device A) and one with debug firmware (device B) flashed on them.
  
  0b. Get the finger clip ready and instruct the volunteer to rest their arm on the table and not move during the measurement. 
  
  1. Perform a simple attributed data test on a sample using the device A.
  IF the output of device A seems reasonable, switch the finger clip to the device B.
  2. Read the data into your PC and save the log file.
  3. perform this procedure in both finger clip orientations on the index finger and on the pinky (4 measurements all together).
  
  Repeat this procedure on **X** samples and then run the SQI_stats.py code to perform SQI analysis through the whole database. Perform statistical analysis to find 95% confidence interval.
