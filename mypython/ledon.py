# ledon.py - red led on
#
# Feather Huzzah: 
# Pin #0 red LED for general purpose blinking. 
# Pin #2 blue LED for bootloading debug & general purpose blinking
# 2017_0507 PePo new
import digitalio
import board

# maak een led-object
redLed = digitalio.DigitalInOut(board.GPIO0)
# led is een "output"
redLed.switch_to_output()
# make light leds opposite each other
redLed.value = False
