# demos with Yurobot Easy Module shield v1 on top of Metro Express
# 2017-0721 PePo new
import time
import gc

try:
    ''' Blinking RED-led, Ctrl-C to stop
    print('Blinky-red demo...')
    import blinky   # blinky Yurobot RED-LED, Cntrl-C abort
    #'''

    #''' 2017-0819 blinky onboard Neopixel
    #import blinkneopixel

    ''' buzzer demo, Ctrl-C to stop
    print('Buzzer demo...')
    import buzzerdemo
    #'''

    #''' blinking red & blue LEDS, Ctrl-C to stop
    print('LEDs demo...')
    import ledsdemo   # LEDS demo, OK
    #'''

    ''' LED matrix smileys, Ctrl-C to stop
    print('Smileys demo...')
    import smileys 
    time.sleep(0.5) #wait a little time
    smileys.clear(smileys.lefteye)
    smileys.clear(smileys.righteye)
    #'''

    ''' TODO: bar-LED demo
    print('Bargraph demo...')
    import bargraphdemo
    #'''

    ''' ICONS demo on matrices, Ctrl-C to stop
    #import weatherdemo #problem: number display turned
    print('Weather icons demo...')
    import weathericonsdemo
    #'''

    ''' Smiley ICONS demo, Ctrl-C to stop
    print('Smiley icons demo...')
    import smileyiconsdemo
    #'''

except:
    gc.collect()
    print('mem free:', gc.mem_free())
