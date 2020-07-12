# Raspberry Pi RGB LED with Flask
Flask Application with Raspberry Pi and RGB LED

![Circuit](https://github.com/kranok-dev/RPi_RGB_Flask/blob/master/Circuit.png?raw=true)

**Hardware**
* Raspberry Pi (3B+ was used, any other version should work)
* RGB LED
* 3 resistors of 330 Ω 
* 1 Breadboard and 4 jumper wires

**Description**                                                               
> This application consists on running a Web Page using Flask with Python to control an RGB LED. Instead of using the PWM GPIO pins, I used threads to simulate the modulation of pulses for each color channel. Additionally, there is a code to open a USB camera and monitor the RGB LED.

**Installation**
> The implemented code requires Flask and OpenCV to be installed in Python:
  ```
  $ sudo apt-get install python3-flask
  
  $ sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5 python3-dev
  
  $ sudo pip3 install opencv-contrib-python==4.1.0.25
  ```

**Execution**
> For execution, it only requires to clone de repository and running the application:
```
$ sudo python3 app.py
```
> If the camera wants to be used, run:
```
$ python3 Camera.py
```
> To vary the color intensities, open the chromium browser and go to: 
```
localhost:5000
```
> move the slider bars, and enjoy the show!

**Demo Video**
> https://www.youtube.com/watch?v=QwUokBQ-1og
