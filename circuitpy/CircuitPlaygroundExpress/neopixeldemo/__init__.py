# definitions
import math
import time
import ustruct

import board
import busio
import digitalio

import adafruit_lis3dh
import neopixel

ACCEL_RANGE   = adafruit_lis3dh.RANGE_16_G
_TAP_THRESHOLD = const(20)
SPINNER_DECAY = 0.5

# 0 <= brightness <= 255
BRIGHTNESS = 125

#colors
RED = (BRIGHTNESS, 0, 0)
GREEN = (0, BRIGHTNESS, 0)
BLUE = (0, 0, BRIGHTNESS)

# Initialize and turn off NeoPixels.
def initpixels():
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
    blank(pixels)
    return pixels

def setpixels(np, color):
    np.fill(color)
    np.write()

def blank(np):
    setpixels(np, (0,0,0))

# run-time
np = initpixels()

setpixels(np, BLUE)
time.sleep(0.2)

blank(np)
print('neopixeldemo: Done!')
