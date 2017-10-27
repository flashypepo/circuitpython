# read the lightsensor
# based upon: https://learn.adafruit.com/fidget-spinner-tachometer/circuitpython
import board, analogio, time
import array

SAMPLE_DEPTH = 25 #256

# Configure analog input for light sensor.
light = analogio.AnalogIn(board.LIGHT)

# Take an initial set of readings and measure how long it takes.
# Use the array module to preallocate an array of 16-bit
# unsigned samples with lower memory overhead vs. a simple python list.

# Convert the analog reading (which goes from 0 to 65535) to a resistor value for the sensor
# ref. 10K
_MAX_VALUE = const(65535)
#_MAX_VALUE = const(1023) #LDR35 / 5598
def Rsensor(value):
    return (_MAX_VALUE - value)*10/value

readings = array.array('H', [0]*SAMPLE_DEPTH)
start = time.monotonic()
for i in range(SAMPLE_DEPTH):
    #readings[i] = int(Rsensor(light.value))
    readings[i] = light.value
stop = time.monotonic()
print('stop-start= {0:0.2f}'.format((stop-start)*1000.0), 'ms')
print ('Readings=', readings)
