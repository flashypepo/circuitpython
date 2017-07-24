# demos with Yurobot Easy Module shield v1 on top of Metro Express
# 2017-0721 PePo new
import time
import gc

#import blinky   # blinky Yurobot RED-LED, OK
#import buzzerdemo  # buzzer demo, Ctrl-C to stop, OK
#import ledsdemo   # LEDS demo, OK

''' LED matrix smileys, OK
import smileys 
time.sleep(0.5) #wait a little time
smileys.clear(smileys.lefteye)
smileys.clear(smileys.righteye)
#'''
''' bar-LED demo
import bargraphdemo
#'''

#''' ICONS demo on matrices
import iconsdemo
#'''
gc.collect()
print('mem free:', gc.mem_free())
