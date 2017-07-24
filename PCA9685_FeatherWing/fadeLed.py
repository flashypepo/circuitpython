# fadeLed.py - fade a led using pca9685 PWM and servo featherwing
# 2017_0205 CircuitPython version
# source: https://learn.adafruit.com/micropython-hardware-pca9685-pwm-and-servo-driver/software

import time

# Adafruit CircuitPython I2C Initialization
from board import *
import bitbangio as io # Huzzah ESP8266 uses soft I2C
i2c = io.I2C(SCL, SDA)

#Import PCA9685 Module
from adafruit_pca9685 import pca9685

# LED on servo-port 0
pca = pca9685.PCA9685(i2c)
pca.freq(60) # for LED set board's PWM frequency to 60hz

# control the LED brightness by controlling
# the duty cycle of the channel connected to the LED
# LED: channel=0
pca.duty(0, 4095) # LED completely on
time.sleep(3)       # 3 seconds
pca.duty(0, 1000) # LED dimmed
time.sleep(3)       # 3 seconds
pca.duty(0, 0)    # LED off
time.sleep(1)       # 1 second

# LED glow on/off
def glow(channel, delay):
    while True:
        # Ramp up in brightness:
        for i in range(4096):
            pca.duty(channel, i)
            time.sleep(delay)
        # Ramp back down in brightness:
        for i in range(4094, 0, -1):
            pca.duty(channel, i)
            time.sleep(delay)
glow(0, 0.001)
