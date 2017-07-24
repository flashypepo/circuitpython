# testServo.py - test servo on channel using pca9685
#                PWM and servo featherwing
# 2017_0205 CircuitPython version
# source: https://learn.adafruit.com/micropython-hardware-pca9685-pwm-and-servo-driver/software

import time

# Adafruit CircuitPython I2C Initialization
from board import *
import bitbangio as io # Huzzah ESP8266 uses soft I2C
i2c = io.I2C(SCL, SDA)

# Import Servo Module
from adafruit_pca9685 import servo
servos = servo.Servos(i2c)

# There are a few ways to control the position of the servo
# using the position function. One way is to specify the
# pulse length in microseconds. Most servos will go to their
# center position at a pulse length of 1500 microseconds,
# a 90 degree extreme at 2000 microseconds,
# and the opposite 90 degree extreme at 1000 microseconds.

# Try setting the servo to its center position with a
# pulse length of 1500 microseconds.
# Servo is connected to channel 5
CHANNEL = 5
servos.position(CHANNEL, us=1500)
time.sleep(1.0)

# Try other extremes like 2000 and 1000 microseconds
# to see how the servo moves:
servos.position(CHANNEL, us=2000)
time.sleep(1.0)
servos.position(CHANNEL, us=1000)
time.sleep(1.0)

# You can also specify a position as an angle.
# This is a little trickier to use since you'll need
# to know the total angle that your servo can sweep between.
# The default is 180 degrees but your servo might have a
# smaller sweep--change the total angle by specifying the
# degrees parameter in the Servos class initializer above.
servos.position(CHANNEL, degrees=180)
time.sleep(1.0)
servos.position(CHANNEL, degrees=0)
time.sleep(1.0)

# sweep servo between 0 and 180 degrees
def sweep(channel, delay):
    while True:
        for i in range(180):
            servos.position(channel, degrees=i)
            time.sleep(delay)
        for i in range(180, 0, -1):
            servos.position(channel, degrees=i)
            time.sleep(delay)
sweep(5, 0.005)
