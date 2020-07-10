# RPi_RGB_Flask
Flask Application with Raspberry Pi and RGB LED

Author: **KB Kwan Loo**              
Date of creation: July, 2020                                                         

**Description**                                                               
> TThis application consists on running a Web page using Flask with Python to control an RGB LED. Instead of using the PWM GPIO pins, I used threads to simulate the modulation of pulses for each color channel. Additionally, there is a code to open a USB camera and monitor the RGB LED.

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
>To vary the color intensities, open the chromium browser and go to 
```
localhost:5000
```
> move the slider bars, and enjoy the show!
