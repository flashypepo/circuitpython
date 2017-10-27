import board
import digitalio  #2017-1021 PePo deprecated: nativeio
#2017-1021 PePo: board.LEFT/RIGHT_BUTTON renamed _A and _B

import neopixel


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
#2017-1021 deprecated left_button = nativeio.DigitalInOut(board.LEFT_BUTTON)
left_button = digitalio.DigitalInOut(board.BUTTON_A)
#left_button.switch_to_input(pull=digitalio.DigitalInOut.Pull.DOWN)
left_button.switch_to_input(pull=digitalio.Pull.DOWN)

right_button = digitalio.DigitalInOut(board.BUTTON_B)
#right_button.switch_to_input(pull=digitalio.DigitalInOut.Pull.DOWN)
right_button.switch_to_input(pull=digitalio.Pull.DOWN)

slide_switch = digitalio.DigitalInOut(board.SLIDE_SWITCH)
slide_switch.switch_to_input(pull=digitalio.Pull.UP)
