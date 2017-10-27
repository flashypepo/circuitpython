# example Yurobot Easy Module shield v1 on top of Metro Express
# URL: 
# 2017-0624 PePo test LEDS
import digitalio
import board
import time
# define leds on the shield
# LED: D12, D13, RGB-LED: D9-D11
leds = [digitalio.DigitalInOut(board.D12), 
        digitalio.DigitalInOut(board.D13),
        digitalio.DigitalInOut(board.D9),
        digitalio.DigitalInOut(board.D10),
        digitalio.DigitalInOut(board.D11)
        ]
# configure led-pins
for led in leds:
    led.switch_to_output()
# alternate led-values
leds[0].value = True
#leds[2].value = False# RED
leds[3].value = True # GREEN
#leds[4].value = True # BLUE
# blink all leds
for i in range(12):
    #while True:
    for led in leds:
        #print('LED value={0}'.format(led.value))
        led.value = not led.value
        time.sleep(0.5)

# leds off
time.sleep(1.0)
for led in leds:
    led.value = False

print('Done!')
