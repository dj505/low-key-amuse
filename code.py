import time
import board
import busio
import adafruit_mpr121
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

i2c = busio.I2C(board.GP21, board.GP20)
mpr121 = adafruit_mpr121.MPR121(i2c)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Config
player_side = 1

# Pin mappings correspond to keypad keys from left to right, top to bottom.
# Most of the keycodes you'll need can be found at:
# https://docs.circuitpython.org/projects/hid/en/latest/_modules/adafruit_hid/keycode.html
pin_mapping_p1 = {
    3:  Keycode.KEYPAD_SEVEN,
    4:  Keycode.KEYPAD_EIGHT,
    8:  Keycode.KEYPAD_NINE,
    2:  Keycode.KEYPAD_FOUR,
    5:  Keycode.KEYPAD_FIVE,
    9:  Keycode.KEYPAD_SIX,
    1:  Keycode.KEYPAD_ONE,
    7:  Keycode.KEYPAD_TWO,
    10: Keycode.KEYPAD_THREE,
    0:  Keycode.KEYPAD_ZERO,
    6:  Keycode.KEYPAD_ENTER,
    11: Keycode.KEYPAD_PERIOD,
}

pin_mapping_p2 = {
    3:  Keycode.I,
    4:  Keycode.O,
    8:  Keycode.P,
    2:  Keycode.J,
    5:  Keycode.K,
    9:  Keycode.L,
    1:  Keycode.B,
    7:  Keycode.N,
    10: Keycode.M,
    0:  Keycode.COMMA,
    6:  Keycode.PERIOD,
    11: Keycode.FORWARD_SLASH,
}

key_map = pin_mapping_p1

if player_side == 2:
    key_map = pin_mapping_p2

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

while True:
    for i in range(12):
        if mpr121[i].value:
            keyboard.press(key_map[i])
            led.value = True
        else:
            keyboard.release(key_map[i])
            led.value = False
