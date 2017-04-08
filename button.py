import RPi.GPIO as GPIO
import time
from time import sleep
from picamera import PiCamera
import datetime
import time

date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
        input_state = GPIO.input(21)
        camera = PiCamera()
        if input_state == False:
                print("button pressed")
                time.sleep(0.2)
                camera.rotation = 270
                camera.start_preview ()
                camera.preview_fullscreen = True
                camera.preview_alpha = 255
                camera.stop_preview()
                print("Foto")
                camera.capture('/home/pi/Desktop/'+ date + '.jpg' )
                        
