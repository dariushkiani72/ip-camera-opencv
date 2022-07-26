# ip-camera-opencv
In this article, it is explained how to connect the IP camera to the computer and display it with Python(opencv). (with the code)


How to connect the ip camera with Python
   Items needed:
•	network cable
•	Ip camera
•	Adapter
 
<div id="badges">
  <img src="https://github.com/dariushkiani72/ip-camera-opencv/blob/main/item%20ip.jpg"  width="500" height="360"/>
</div>

How to connect:
The network camera used has three plugs, one for power supply, we connect to the 12V 2A adapter, the second to connect to the network,
we connect one end of the network cable to the camera and the other to the computer network. In some cameras, there is no power connection,
to power the camera through a network cable, we need to use a rotor or power switch (PoE), and the third one is for sound, which is not used for us.

IP camera:
Each camera has its own IP network. Usually, when buying a camera, there is information with it, such as the camera's IP, name, and password required to enter
, which are required for connection.


Find IP address:
Using (wireshark) network protocol analyzer
This software displays the information that is sent to packet capture, we install the software, connect the camera, and after opening the software,
select the local area connection option and run it.
Connecting the camera to the dvr is another that provides us with the IP of the camera.

Add IP camera image
cap = cv2.VideoCapture('rtsp://name:password@ip/1')
We used the VideoCapture command of the opencv library.
import cv2
import numpy as np


cap = cv2.VideoCapture('rtsp://admin:1234@192.168.1.***/1')

