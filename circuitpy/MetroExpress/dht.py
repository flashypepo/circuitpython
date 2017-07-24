# example Yurobot Easy Module shield v1 on top of Metro Express
# URL: 
# 2017-0624 PePo test LEDS
import digitalio
import board
import time
import dht
import machine

d = dht.DHT11(machine.Pin(4))
d.measure()
d.temperature() # eg. 23 (°C)
d.humidity()    # eg. 41 (% RH)

print('Done!')
