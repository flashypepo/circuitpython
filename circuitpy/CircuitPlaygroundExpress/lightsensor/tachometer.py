# Adafruit Circuit Playground Express Fidget Spinner Tachometer
#
# This code uses the light sensor built in to Circuit Playground Express
# to detect the speed (in revolutions per second) of a fidget spinner.
# Save this code as main.py on a Circuit Playground Express board running
# CircuitPython (see https://github.com/adafruit/circuitpython).  You will
# also need to load neopixel.mpy onto the board's filesystem (from
# https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel/releases).
#
# When the first three NeoPixels light up white you're ready to read the speed # of a spinner. Hold a spinning fidget spinner very close to (but not touching)
# the light sensor (look for the eye graphic on the board, it's right
# below the three lit NeoPixels) and look at the serial terminal from the board
# at 115200 baud to see the speed of the spinner printed.  This works best
# holding the spinner perpendicular to the sensor, like:
#       ||
#       || <- Spinner
#       ||
#    ________  <- Circuit Playground
#
# Author: Tony DiCola
# License: MIT License (https://en.wikipedia.org/wiki/MIT_License)
import array

import board
import analogio
import time

import neopixel


# Configuration:
SPINNER_ARMS           = 3       # Number of arms on the fidget spinner.
                                 # This is used to calculate the true
                                 # revolutions per second of the spinner
                                 # as one full revolution of the spinner
                                 # will actually see this number of cycles
                                 # pass by the light sensor.  Set this to
                                 # the value 1 to ignore this calculation
                                 # and just see the raw cycles / second.

SAMPLE_DEPTH           = 256     # How many samples to take when measuring
                                 # the spinner speed.  The larger this value
                                 # the more memory that will be consumed but
                                 # the slower a spinner speed that can be
                                 # detected (larger sample depths mean longer
                                 # period waves can be detected).  You're
                                 # limited by the amount of memory on the
                                 # board for this value.

TARGET_SAMPLE_RATE_HZ  = 150     # Target sample rate for sampling the light
                                 # sensor.  This in combination with the sample
                                 # depth above controls how slow and fast of
                                 # a signal you can detect.  Note that the
                                 # sample rate can only go so high before it's
                                 # too fast for the Python interpreted code
                                 # to run.  If that happens the board will
                                 # light up LEDs red to indicate the 'underflow'
                                 # condition (drop the sample rate down to
                                 # a lower value and try again).
                                 # A value of 150 times a second means you can
                                 # measure a spinner going up to 25 revolutions
                                 # per second.

THRESHOLD              = 40000   # How big the magnitude of a cyclic
                                 # signal has to be before the measurement
                                 # logic kicks in.  This is a value from
                                 # 0 to 65535 and might need to be adjusted
                                 # up or down if the detection is too
                                 # sensitive or not sensitive enough.
                                 # Raising this value will make the detection
                                 # less sensitive and require a very large
                                 # difference in amplitude (i.e. a very close
                                 # or highly reflective spinner), and lowering
                                 # the value will make the detection more
                                 # sensitive and potentially pick up random
                                 # noise from light in the room.


# Configure NeoPixels and turn them all off at the start.
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.fill((0,0,0))
pixels.write()

# Configure analog input for light sensor.
light = analogio.AnalogIn(board.LIGHT)

# Take an initial set of readings and measure how long it takes.
# This is used to calculate a delay between readings to hit the desired
# target sample rate.  Use the array module to preallocate an array of 16-bit
# unsigned samples with lower memory overhead vs. a simple python list.
readings = array.array('H', [0]*SAMPLE_DEPTH)
start = time.monotonic()
for i in range(SAMPLE_DEPTH):
    readings[i] = light.value
stop = time.monotonic()
print((stop-start)*1000.0)

# Calculate how long it took to take all the readings above, then figure out
# the difference from the target period to actual period.  This difference is
# the amount of time to delay between sample readings to hit the desired target
# sample rate.
target_period = 1.0/TARGET_SAMPLE_RATE_HZ
actual_period = (stop-start)/SAMPLE_DEPTH
delay = 0
# Check that we can sample fast enough to hit the target rate.
if actual_period > target_period:
    # Uh oh can't sample fast enough--print a warning and light up pixels red.
    print('Could not hit desired target sample rate!')
    pixels.fill((255,0,0))
    pixels.write()
else:
    # No problem hitting target sample rate so calculate the delay between
    # samples to hit that desired rate.  Then turn on the first three pixels
    # to white full brightness.
    delay = target_period - actual_period
    pixels[0] = (255, 255, 255)
    pixels[1] = (255, 255, 255)
    pixels[2] = (255, 255, 255)
    pixels.write()

# Main loop:
while True:
    # Pause for a second between tachometer readings.
    time.sleep(1.0)
    # Grab a set of samples and measure the time it took to do so.
    start = time.monotonic()
    for i in range(SAMPLE_DEPTH):
        readings[i] = light.value
        time.sleep(delay)  # Sleep for the delay calculated to hit target rate.
    stop = time.monotonic()
    elapsed = stop - start
    # Find the min and max readings from the samples.
    minval = readings[0]
    maxval = readings[0]
    for r in readings:
        minval = min(minval, r)
        maxval = max(maxval, r)
    # Calculate magnitude or size of the signal.  If the magnitude doesn't
    # pass the threshold then start over with a new sample (run the loop again).
    magnitude = maxval - minval
    if magnitude < THRESHOLD:
        continue
    # Calculate the midpoint of the signal, then count how many times the
    # signal crosses the midpoint.
    midpoint = minval + magnitude/2.0
    crossings = 0
    for i in range(1, SAMPLE_DEPTH):
        p0 = readings[i-1]
        p1 = readings[i]
        # Check if a pair of points crossed the midpoint either by hitting it
        # exactly or hitting it going up or down.
        if p1 == midpoint or p0 < midpoint < p1 or p0 > midpoint > p1:
           crossings += 1
    # Finally use the number of crosssings and the amount of time in the sample
    # window to calculate how many times the spinner arms crossed the light
    # sensor.  Use that period to calculate frequency (rotations per second)
    # and RPM (rotations per minute).
    period = elapsed / (crossings / 2.0 / SPINNER_ARMS)
    frequency = 1.0/period
    rpm = frequency * 60.0
    print('Frequency: {0:0.5} (hz)\t\tRPM: {1:0.5}\t\tPeriod: {2:0.5} (seconds)'.format(frequency, rpm, period))
