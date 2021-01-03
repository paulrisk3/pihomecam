# pihomecam
Video streaming from Pi camera over HTTP

## Getting Started

### Prerequisites
<code>sudo apt-get install python-picamera python3-picamera</code>

### Installation
<code>git clone https://github.com/paulrisk3/pihomecam.git</code>

## Usage
<code>cd pihomecam</code>
<code>sudo python pihomecam.py</code>

### Run as a Service (run at startup)
<code>cp pihomecam.service /etc/systemd/system/</code>
<code>systemctl enable pihomecam.service</code>
<code>systemctl start pihomecam.service</code>

Verify functionality with <code>systemctl status pihomecam.service</code>

## To do

## Old Readme
Install necessary packages:\
  <code> sudo apt-get update </code>\
  <code>sudo apt-get install python-picamera python3-picamera</code>
  
Clone pihomecam and test web stream:\
  <code> git clone https://github.com/paulrisk3/pihomecam.git </code>\
  <code> cd pihomecam </code>\
  <code> sudo python pihomecam.py </code>
  
Open a browser and navigate to: <code> 127.0.0.1:8000 </code>\
Can also be on a computer in your network and go to raspbery_pi_ip:8000/stream.mjpg in a local broswer



Setup Service to run constantly:

<code> cp pihomecam.service /etc/systemd/system/ </code>\
<code> systemctl enable pihomecam.service </code>\
<code> systemctl start pihomecam.service </code>




  
  
















For further learning and walkthroughs visit (where I learned most of the things I used): https://picamera.readthedocs.io/en/latest/quickstart.html
