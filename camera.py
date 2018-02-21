from picamera import PiCamera
from time import sleep

camera = PiCamera()

##camera.resolution = (1713, 800)
##camera.framerate = 49
##camera.start_preview()
##sleep(5)
##camera.capture('/home/pi/Desktop/max.jpg')
##camera.stop_preview()
##
##
##camera.start_preview()
##camera.annotate_text = "Hello y'all!"
##sleep(5)
##camera.capture('/home/pi/Desktop/text.jpg')
##camera.stop_preview()
##
##camera.start_preview(alpha = 200)
##camera.brightness = 100
##sleep(5)
##camera.capture('/home/pi/Desktop/bright.jpg')
##camera.stop_preview()
##
##camera.start_preview()
##for i in range(100):
##    camera.annotate_text
##camera.start_preview()
##sleep(5)
##camera.stop_preview()

##camera.start_preview(alpha=200)
##sleep(10)
##camera.stop_preview()
##camera.start_preview()
##sleep(5)
##camera.capture('/home/pi/Desktop/image.jpg')
##camera.stop_preview()
##
##camera.start_preview()
##for i in range(5):
##    sleep(5)
##    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
##camera.stop_preview()
##
##camera.start_preview()
##camera.start_recording('/home/pi/video.h264')
##sleep(5)
##camera.stop_recording()
##camera.stop_preview()

camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()

camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
sleep(5)
camera.stop_preview()
