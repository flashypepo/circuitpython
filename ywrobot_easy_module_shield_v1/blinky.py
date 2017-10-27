import digitalio
import board
import time

#led = digitalio.DigitalInOut(board.D13)
led = digitalio.DigitalInOut(board.D12)
led.switch_to_output()
while True:
    led.value = not led.value
    time.sleep(0.5)