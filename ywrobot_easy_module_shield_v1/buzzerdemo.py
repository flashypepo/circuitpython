# example Yurobot Easy Module shield v1 on top of Metro Express
# URL: 
# 2017-0624 PePo test buttons SW1 and SW2
import digitalio
import board
import time
import pulseio

# SETUP
print('Start buzzer demo...')

# Configure PWM buzzer and other state:
BUZZER_PIN = board.D5
# Duty cycle of tone when turned on, a square wave.
TONE_ON_DUTY  = 2**15
# Duty cycle of tone when turned off, 0 or no signal.
TONE_OFF_DUTY = 0
# tones
NOTE_FREQS = [ 261,  # Input 0 = 261 hz = middle C
               294,  # Input 1 = middle D
               329,  # Input 2 = middle E
               349,  # Input 3 = middle F
               392,  # Input 4 = middle G
               440,  # Input 5 = middle A
               493,  # Input 6 = middle B
               0]    # Input 7 = 0, no tune
               
# Setup buzzer PWM output.
buzzer = pulseio.PWMOut(BUZZER_PIN, duty_cycle=TONE_OFF_DUTY, frequency=440,variable_frequency=True)

# Setup two buttons SW1, SW2 on D2, D3
sw1 = digitalio.DigitalInOut(board.D2)
sw2 = digitalio.DigitalInOut(board.D3)
sw1.switch_to_input(pull=digitalio.Pull.UP) #input UP
sw2.switch_to_input(pull=digitalio.Pull.UP) #input UP

# Setup RGB-led on D9-D11
rgbled = [ digitalio.DigitalInOut(board.D9),
        digitalio.DigitalInOut(board.D10),
        digitalio.DigitalInOut(board.D11)]
# leds are output
for led in rgbled:
    led.direction = digitalio.Direction.OUTPUT

#LOOP: wait for button press, then light on RGB and buzzer
import math
print('Press button s1 of sw2...')
while True:
    for led in rgbled:
        led.value = False
    buzzer.duty_cycle = TONE_OFF_DUTY
    
    if not sw1.value:
        print("sw1 pressed")
        rgbled[0].value = True
        freq = NOTE_FREQS[0] # grab note
    elif not sw2.value:
        print("sw2 pressed")
        rgbled[2].value = True
        freq = NOTE_FREQS[1] # grab note
    else:
        rgbled[1].value = True
        freq = NOTE_FREQS[7] # nothing
        
    if freq != 0:
        buzzer.frequency = freq
        buzzer.duty_cycle = TONE_ON_DUTY
        
    time.sleep(0.1)
    #time.sleep(0.01)
