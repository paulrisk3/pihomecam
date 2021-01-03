# pihomecam
Video streaming from Pi camera over HTTP

## Getting Started

### Prerequisites
<code>sudo apt-get install python-picamera python3-picamera</code>

### Installation
<code>git clone https://github.com/paulrisk3/pihomecam.git</code>

## Usage

### Run Camera
* <code>cd pihomecam</code>
* <code>sudo python pihomecam.py</code>

### Run as a Service (run at startup)
* <code>cp pihomecam.service /etc/systemd/system/</code>
* <code>systemctl enable pihomecam.service</code>
* <code>systemctl start pihomecam.service</code>
* Verify functionality with <code>systemctl status pihomecam.service</code>

### Access Video Stream
* On a web browser on the same network as the Pi Cam, navigate to `<PiCam IP>`:8000/stream.mjpg

## To do
* Protect against DDOS attacks
* Provide authentication to access stream
* Stream over HTTPS instead of HTTP?
* Optimize video stream to reduce bandwith

For further learning and walkthroughs visit (where I learned most of the things I used): https://picamera.readthedocs.io/en/latest/quickstart.html
