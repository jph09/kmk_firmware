print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.hid import HIDModes
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0,)
keyboard.row_pins = (board.D1,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

split = Split(split_type=SplitType.BLE)

keyboard.modules = [split]

keyboard.keymap = [
    [KC.A,KC.B,]
]

if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE, ble_name="KMKeyboard")
