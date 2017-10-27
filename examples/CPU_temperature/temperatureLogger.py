# logging temperature in file
# requires READONLY access to filesystem is FALSE
#  -> boot with switch D7 grounded, see boot.py
#
# 2017-1023  PePo new, added device READONLY and method run()
# source: https://learn.adafruit.com/cpu-temperature-logging-with-circuit-python?view=all
# TODO: add better error reporting (the OSError error code for a read only device is 30).

import board
import digitalio
import microcontroller
import time

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()

def run():
    try:
        with open("/temperature.txt", "a") as fp:
            while True:
                temp = microcontroller.cpu.temperature
                # do the C-to-F conversion here if you would like
                fp.write('{0:f}\n'.format(temp))
                fp.flush()
                led.value = not led.value
                time.sleep(1)
    except OSError as e:
        delay = 0.5
        if e.args[0] == 28: # device is out of space
            delay = 0.25
        if e.args[0] == 30:
            delay = 0.1 # device is READONLY
        while True:
            led.value = not led.value
            time.sleep(delay)

''' usage: 
import temperatureLogger
temperatureLogger.run()
#'''
