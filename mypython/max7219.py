# max7219.py - voorbeeld Max7219 aansturing in CircuitPython
# 2017_0121 PePo new Adafruit Huzzah ESP8266
# bron: http://micropython-max7219.readthedocs.io/en/latest/examples.html

#Max7219 LED Matrix libraries
import max7219
from machine import Pin, SPI

#utility libraries
from time import sleep

def setupLedMatrix():
    spi = SPI(-1, 10000000, miso=Pin(12), mosi=Pin(13), sck=Pin(14))
    display = max7219.Matrix8x8(spi, Pin(2))
    return display
display = setupLedMatrix()

def setupLed():
    #led = nativeio.DigitalInOut(board.GPIO5)
    led = Pin(5, Pin.OUT)    # create output pin on GPIO5
    return led
led = setupLed()

# alle pixels uit
# aangezien kleur 1 of 0 is (B/W),
# kan True / False gebruikt worden
def off():
    display.fill(False) #alles uit
    display.show()

#0<= value <= 15
#see https://github.com/adafruit/micropython-adafruit-max7219/blob/1606b2ad3e47b349e21acbe4752e51aec6d874dd/max7219.py
def setBrighness(v):
    display.brightness(v)

#zet pixels op hoekpunten aan/uit..
def setCorners(d, color):
    # pixel(x, y, color=None)
    d.pixel(0,0,color)
    d.pixel(0,7,color)
    d.pixel(7,0,color)
    d.pixel(7,7,color)

# zet middelste pixel aan/uit...
def setCenter(d, color):
    d.pixel(3, 3, color)
    d.pixel(3, 4, color)
    d.pixel(4, 3, color)
    d.pixel(4, 4, color)

# main loop
while True:
    # zet led aan
    led.value(False)
    off()
    
    setCorners(display, True)
    setCenter(display, True)
    display.show() # update the display

    sleep(1) #wait
    
    #zet led uit
    led.value(True)

    setCorners(display, False)
    setCenter(display, False)
    display.show() # update the display
    sleep(0.5) #wait
