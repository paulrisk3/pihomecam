import picamera
import datetime
## from subprocess import call

horizontalResolution = 1280
verticalResolution = 720
framerate = 10
recordLength = 10

## Initialize camera at max resolution
camera = picamera.PiCamera(resolution=(horizontalResolution, verticalResolution), framerate=framerate)
## Capture recordings forever (until stopped)
## I need to delete old recordings. Target is a week of recordings.
while True:
  filename = ('recordings/' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S"))
  camera.start_recording(filename + '.h264')
  camera.wait_recording(recordLength)
  camera.stop_recording()
  ##command = "MP4Box -add '{0}'.h264 '{1}'.mp4".format(filename, filename)
  ##call([command], shell=True)
