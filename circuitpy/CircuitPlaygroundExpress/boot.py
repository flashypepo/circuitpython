# make it boot.py and CircuitPython is allowed to write
# to filesystem, if switch is grounded
# This must be code executed during boot, before USB is created.
# 2017-1023 PePo new, adopted to Circuit Playground Express
# source:
# https://learn.adafruit.com/cpu-temperature-logging-with-circuit-python?view=all

import digitalio
import board
import storage

# Gemma M0: switch = digitalio.DigitalInOut(board.D0)
switch = digitalio.DigitalInOut(board.D7) #adopted for playground switch
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

# If the switch is connected to ground with a wire
# CircuitPython can write to the drive
storage.remount("/", switch.value)
