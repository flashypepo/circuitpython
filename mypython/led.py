# led.py - eenvoudig voorbeeld met CircuitPython
#
# led op pin GPIO14
# 2017_0121 PePo new
import board
import nativeio

# maak een led-object
led = nativeio.DigitalInOut(board.GPIO2)
# led aan- of uitzetten vanuit controller: led is een "output"
led.switch_to_output()
# zet led aan
led.value = True

#zet led uit
led.value = False
