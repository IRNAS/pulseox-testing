# 2 DEBUGGING

Debug firmware allows you to output the data from your GliaX pulse oximeter to your PC via USB to RS232 levels serial UART converter and visualize them. For this you will need to have installed a serial terminal ([Termite](https://www.compuphase.com/software_termite.htm) or similar) and [Pyhon 3.X](http://winpython.github.io/). You will also need a UART bridge.

<img src="https://user-images.githubusercontent.com/14543226/31599088-24b45666-b251-11e7-815b-aab835faab1b.jpg" alt="settings" width= "250" >

|USB-RS232| GliaX|
|:----:|:----:|
|5V (not needed if powered from USB or battery)|5V|
|TXD|CK|
|RXD (not needed)|IO|
|GND|GND|

1. Open a serial terminal (Termite is used in this demonstration)
2. Press 'Settings'
3. Configure your port (select the right COM port on your computer. On Windows OS you can check which port you are using in device manager.)

<img src="https://user-images.githubusercontent.com/14543226/31546850-64932e5c-b025-11e7-800d-1ce65178edc3.PNG" alt="settings" width= "350" >

4. tick the 'Log File' and double click it, then set the log file name and location. Let's assume you have set your file name to 'MyLogFile'
5. Click 'OK'
6. Plug your UART bridge into your PC which must be hooked up to your GliaX as shown in the table above. 
7. Power your pulse oximeter either from the battery or DC power supply on the BAT pins, or via microUSB cable and turn the switch on
8. Follow the instructions on the display.
9. You should see a series of numbers running down your PC screen. They will all be saved in a 'MyLogFile' at the location you specified in step 4. 

10. Go to log file location and rename 'MyLogFile' file by adding a '.txt' to the end of the name.
11. Open the MyLogFile.txt
12. Delete the few rows header "Debug console enabled..." etc. so that you are only left with numbers. This is important in order not to get errors during the data processing later on.
