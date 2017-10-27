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
    print('Blinky-neopixel demo...')
    import blinkneopixel
    #''' 
    
    ''' buzzer demo, Ctrl-C to stop
    print('Buzzer demo...')
    import buzzerdemo
    #'''

    ''' blinking red & blue LEDS, Ctrl-C to stop
    print('LEDs demo...')
    import ledsdemo   # LEDS demo, OK
    #'''
    
    ''' 2017-0820 LM35 readings
    print('LM35 demo...')
    import lm35
    """ Temperature plm. 25 Celsius
      Reading   Voltage Temperature
        25575   1.29    128.78
        25469   1.28    128.24
        25385   1.28    127.82
        25454   1.28    128.17
        25489   1.28    128.34
        25233   1.27    127.06
        25539   1.29    128.60
        25710   1.29    129.46
    """
    #'''
    
    ''' 2017-0820 analoge readings
    print('Analoge sensors demo...')
    import analogsensors
    """ Temperature plm. 25 Celsius
    -------------------------------------
    Sensor  Reading Voltage Temperature
    Pot     27873   1.40
    LDR     65520   3.30
    LM35    6066    0.31    30.55
    -------------------------------------
    Vreemd: LDR op maximum, LM35 veels te hoog. Potentiometer OK
    lijkt wel of A1 en A2 niet op Metro M0 zijn aangesloten ???
    """
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
