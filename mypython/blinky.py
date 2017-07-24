# blinky.py - blinky led in CircuitPython
#
# Feather Huzzah: 
# Pin #0 red LED for general purpose blinking. 
# Pin #2 blue LED for bootloading debug & general purpose blinking
# 2017_0506 PePo new
import digitalio
import board
import time

# maak een led-object
redLed = digitalio.DigitalInOut(board.GPIO0)
blueLed = digitalio.DigitalInOut(board.GPIO2)

# led is een "output"
redLed.switch_to_output()
blueLed.switch_to_output()

# make light leds opposite each other
redLed.value = False
blueLed.value = True

#loop: toggle leds
while True:
    redLed.value = not redLed.value
    blueLed.value = not blueLed.value
    time.sleep(0.3)
