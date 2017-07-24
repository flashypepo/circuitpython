# OLED1306 demo - CircuitPython
# 2017-0521 based upon Tony DiCola Learning Guide:
# https://learn.adafruit.com/micropython-hardware-ssd1306-oled-display/software
# OLED1306 driver code:
# https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/blob/master/adafruit_ssd1306/ssd1306.py

# import OLED 1306 driver
import adafruit_ssd1306 as ssd1306

# I2C initialization
from board import *
import busio
i2c = busio.I2C(SCL, SDA)
i2c.scan() # test: scan I2C bus

OLED_WIDTH = 128
OLED_HEIGTH = 32
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGTH, i2c)

# clear oled-display with color (default color=0)
def clear(oled, color=0):
    '''clear oled with color (default 0)'''
    oled.fill(color) # display color
    oled.show()
clear(oled)

# pixels at corners
def corners(oled):
    '''draws pixel at the corners of OLED'''
    oled.pixel(0, 0, 1)
    oled.pixel(0, OLED_HEIGTH - 1, 1)
    oled.pixel(OLED_WIDTH - 1, 0, 1)
    oled.pixel(OLED_WIDTH - 1, OLED_HEIGTH - 1, 1)
    oled.show()

#demos
import time

# scrolling text ...
# dx, dy in pixels
print('scrolling demo#1...')
oled.text('Hello Peter', 0, 0)
oled.show()
for x in range(OLED_WIDTH):
    oled.scroll(x, 0)
    time.sleep(0.2)
    oled.show()
clear(oled)

print('scrolling demo#2...')
oled.text('Hello Peter', 0, 0)
oled.show()
for x in range(len('Hello Peter')):
    oled.scroll(-x * 5, 0)
    time.sleep(0.2)
    oled.show()
clear(oled)

lines = OLED_HEIGTH // 8
print('scrolling demo#3... {0}'.format(lines), ' lines')
oled.text('Hello Peter', 0, 0)
oled.show()
for x in range(lines):
    oled.scroll(x * 5, x * 8)
    oled.show()
    time.sleep(0.2)
print('done!')
time.sleep(5)
#clear(oled)

print('scrolling demo#4... scrolll back')
# 2017-0521 werkt niet zoals verwaccht: tekst kwijt!
for i in range(OLED_WIDTH // 5):
    oled.scroll(-i*5,0)
    oled.show()
    time.sleep(0.2)

# de-couple i2c
# ? does it still work?
# 2017-0521; no, so only lateron?
# i2c.deinit()