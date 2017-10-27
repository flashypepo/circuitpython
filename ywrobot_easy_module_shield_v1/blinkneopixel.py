# blink Metro M0 neopixel
# 2017-0819 PePo new
#from micropython import const
import board
import neopixel
import time
import urandom

# blink neopixel, Ctrl-C to interrupt
__MAX_BRIGHTNESS = 50
np = neopixel.NeoPixel(board.NEOPIXEL, 1)
def blink(dt=1.0):
    while True:
        np.fill((0,0,0))
        np.write()
        time.sleep(dt/5)
        r = urandom.randrange(0,__MAX_BRIGHTNESS)
        g = urandom.randrange(0,__MAX_BRIGHTNESS)
        b = urandom.randrange(0,__MAX_BRIGHTNESS)
        #print(r,g,b)
        np.fill((r, g, b))
        np.write()
        time.sleep(dt)
# run
blink()
