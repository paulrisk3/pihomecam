# pihomecam
Quality, consistent video streaming from Pi 0 W camera over HTTP

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

## Stability
This script was designed on a Pi 0 W using a Pi NoIR camera module. I found that, after an undetermined length of running the camera module, the kernel would crash. After some reading, I found that this is an issue seemingly exclusive to the Pi 0 (W or not), and could possibly be mitigated by adding the line <code>over_voltage=6</code> in /boot/config.txt, giving a mild overclock to the single-core Pi CPU. This seems to be working, but just to be safe, I also add <code>kernel.panic=5</code> to /etc/sysctl.conf, to enable the Pi to reboot 5 seconds after a kernel panic event. Neither of these settings should void the warranty on your Pi, but I provide no guarantees regarding stability of longevity of your hardware. 

## To do
* Protect against DDOS attacks
* Provide authentication to access stream
* Stream over HTTPS instead of HTTP?
* Optimize video stream to reduce bandwith (currently transmits 2.0+ MB/s)

For further learning and walkthroughs visit (where I learned most of the things I used): https://picamera.readthedocs.io/en/latest/quickstart.html
