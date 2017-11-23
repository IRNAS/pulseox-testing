# Probe Sensitivity Test

By probe sensitivity testing we test the analog levels of IR and RED signals and the ratio between them (RED/IR). By statistical analysis we will conclude what is an acceptable range of RED and IR levels which will in the future be used for quality control.

We have to produce a table of this sort:

<img src="https://user-images.githubusercontent.com/14543226/33124053-3129ab88-cf7c-11e7-812e-a31aea8ca080.png" alt="table" width= "400" >

First, we need to be able to modify LED intensity by changing the PWM for RED and IR diode separately. Then, we need to sweep the PWMs and obtain the RED and IR PWMs that yield the most stable device performance.
