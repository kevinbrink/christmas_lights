import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)



GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)
# Loop for... Well, a little while anyways ;)
while True:
    GPIO.output(2, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(2, GPIO.LOW)
    time.sleep(2)
