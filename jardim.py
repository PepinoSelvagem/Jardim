import RPi.GPIO as GPIO

import time

    GPIO.setmode(GPIO.BCM)

        GPIO.setwarnings(False)

            GPIO.setup(14,GPIO.OUT)

            print "Vault open"

            GPIO.output(14,GPIO.LOW)

            time.sleep(1000)

            print "Vault closed"

            GPIO.output(14,GPIO.HIGH)
