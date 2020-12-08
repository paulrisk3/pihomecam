import picamera
import datetime
from subprocess import call

horizontalResolution = 768
verticalResolution = 432
framerate = 10
recordLength = 10
format='.h264'

## Initialize camera at max resolution
camera = picamera.PiCamera(resolution=(horizontalResolution, verticalResolution), framerate=framerate)
## Capture recordings forever (until stopped)
## I need to delete old recordings. Target is a week of recordings.
while True:
  filename = ('recordings/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S"))
  camera.start_recording(filename + format)
  camera.wait_recording(recordLength)
  camera.stop_recording()
  # The compression does nothing at all. It's the same size.
  #command = "gzip {0}{1}".format(filename, format)
  #call([command], shell=True)
