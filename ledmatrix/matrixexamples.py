# Examples of clearing and drawing a pixel on a LED matrix display.
#
# CircuitPython
#
# This example and library is meant to work with Adafruit CircuitPython API.
# 2017-0518 PePo - matrix and i2c are already specified
# Author: PePo
# License: Public Domain

# Import all board pins.
from board import *
import busio
import time

# Import the HT16K33 LED matrix module.
from adafruit_ht16k33 import matrix

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
# print I2C devices
i2c.scan()

# Creates a 8x8 matrix:
matrix = matrix.Matrix8x8(i2c, address=0x70) # default I2C address = 0x70
# matrix2 = matrix.Matrix8x8(i2c, address=0x71)
# Finally you can optionally specify a custom I2C address of the HT16k33 like:
# matrix = matrix.Matrix16x8(i2c, address=0x70)

MATRIX_WIDTH = 8  # 8 LEDs
MATRIX_HEIGTH = 8 # 8 LEDs

# running pixel over the matrix
def runningpixel(waitTime=0.5):
    #global matrix
    matrix.fill(0)
    for x in range(MATRIX_WIDTH):
        for y in range(MATRIX_HEIGTH):
            matrix.fill(0)  # blank matrix
            matrix.pixel(x, y, 1) # ledpixel ON at x,y
            matrix.show() # show result
            time.sleep(waitTime) # wait a while

def example2(waitTime=0.5):
    for x in range(MATRIX_WIDTH):
        for y in range(MATRIX_HEIGTH):
            matrix.fill(0)  # blank matrix
            matrix.pixel(x, y, 1) # ledpixel ON at x,y
             # 2nd ledpixel ON from opposite site
            matrix.pixel(MATRIX_WIDTH - x - 1, MATRIX_HEIGTH - y - 1, 1)
            matrix.show() # show result
            time.sleep(waitTime) # wait a while

# all leds ON in matrix
# intensity = 0 .. 15
def full(isOn=1, intensity=8):
    matrix.brightness(intensity)
    matrix.fill(isOn)
    matrix.show()

# all leds OFF in matrix
def blank():
    full(0)

#pattern1 = []
#pattern1 = list(range(0, MATRIX_WIDTH))
#  column       1  2  3  4  5  6  7  8
#pattern1[0] = [1, 0, 0, 0, 0, 0, 0, 0] # top row
#pattern1[1] = [0, 1, 0, 0, 0, 0, 0, 0]
#pattern1[2] = [0, 0, 1, 0, 0, 0, 0, 0]
#pattern1[3] = [0, 0, 0, 1, 0, 0, 0, 0]
#pattern1[4] = [0, 0, 0, 0, 1, 0, 0, 0]
#pattern1[5] = [0, 0, 0, 0, 0, 1, 0, 0]
#pattern1[6] = [0, 0, 0, 0, 0, 0, 1, 0]
#pattern1[7] = [0, 0, 0, 0, 0, 0, 0, 1] # bottom row

# TODO: more efficient to use a bitpattern 0b00111100, and so on
pattern2 = []
pattern2 = list(range(0, MATRIX_WIDTH))
#  column      1  2  3  4  5  6  7  8
pattern2[0] = [0, 0, 1, 1, 1, 1, 0, 0]  # row 1 - top
pattern2[1] = [0, 1, 0, 0, 0, 0, 1, 0]  # row 2
pattern2[2] = [1, 0, 1, 0, 0, 1, 0, 1]  # row 3
pattern2[3] = [1, 0, 0, 0, 0, 0, 0, 1]  # row 4
pattern2[4] = [1, 0, 1, 0, 0, 1, 0, 1]  # row 5
pattern2[5] = [1, 0, 0, 1, 1, 0, 0, 1]  # row 6
pattern2[6] = [0, 1, 0, 0, 0, 0, 1, 0]  # row 7
pattern2[7] = [0, 0, 1, 1, 1, 1, 0, 0]  # row 8 - bottom


# display pattern p on LED-matrix m
def dp(m, p):
    '''show pattern p on matrix m: 0=LED off, 1=LED on'''
    # iterate through sequence...
    for x in range(0, MATRIX_WIDTH):
        # iterate through a row to set led on or off...
        for y in range(0, MATRIX_HEIGTH):
            m.pixel(x, y, p[y][x])
    # show pattern
    m.show()

#displayPattern(matrix, pattern1)
dp(matrix, pattern2)