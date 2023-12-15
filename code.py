print("Starting")

### TO DO ###
# - Momentary swap sides

import board

from kmk.handlers.sequences import send_string
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.oneshot import OneShot
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.tapdance import TapDance
from kmk.scanners import DiodeOrientation


### KEYBOARD ###
keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW

"""
# LEFT SIDE
keyboard.col_pins = (board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9)
keyboard.row_pins = (board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)
split = Split(
    split_flip=False,  # If both halves are the same, but flipped, set this True
    split_side=SplitSide.LEFT,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    split_target_left=True,  # Assumes that left will be the one on USB. Set to False if it will be the right
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP0,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP1,  # Second uart pin to allow 2 way communication
    uart_flip=False,  # Reverses the RX and TX pins if both are provided
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)
"""
# RIGHT SIDE
keyboard.col_pins = (board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9)
keyboard.row_pins = (board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)
split = Split(
    split_flip=False,  # If both halves are the same, but flipped, set this True
    split_side=SplitSide.RIGHT,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    # Switch to False to test right side pins
    split_target_left=True,  # Assumes that left will be the one on USB. Set to False if it will be the right
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP0,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP1,  # Second uart pin to allow 2 way communication
    uart_flip=False,  # Reverses the RX and TX pins if both are provided
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)

keyboard.debug_enabled = True
print("Debugging...")

### MODULES ###
keyboard.modules.append(Combos())
keyboard.modules.append(HoldTap())
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(OneShot())
keyboard.modules.append(split)
keyboard.modules.append(TapDance())


### KEY REMAPPING ###
#OS_LSFT = KC.OS(KC.LSFT)
XXXXXXX = KC.NO

keyboard.coord_mapping = [
     1,  2,  3,  4,  5,  30, 31, 32, 33, 34,
 6,  7,  8,  9, 10, 11,  36, 37, 38, 39, 40, 41,
12, 13, 14, 15, 16, 17,  42, 43, 44, 45, 46, 47,
            21, 22, 23,  48, 49, 50,
    25, 26, 27, 28, 29,  54, 55, 56, 57, 58,
]

### KEYMAP ###
keyboard.keymap = [

    # [0] COLEMAK 
    [
    #       GP14        GP13        GP12        GP11        GP10        GP9      ||     GP14        GP13        GP12        GP11        GP10        GP9
                        KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,           KC.J,       KC.L,       KC.U,       KC.Y,       KC.QUOT,              # GP4
            KC.TAB,     KC.A,       KC.R,       KC.S,       KC.T,       KC.G,           KC.M,       KC.N,       KC.E,       KC.I,       KC.O,      KC.MINS,   # GP5
            KC.LCTL,    KC.Z,       KC.X,       KC.C,       KC.D,       KC.V,           KC.K,       KC.H,       KC.COMM,    KC.DOT,     KC.SLSH,   KC.ENT,    # GP6
                                                KC.A,       KC.B,       KC.C,           KC.X,       KC.Y,       KC.Z,                                         # GP7
                        KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,          KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,                # GP8
    ]
    
]

if __name__ == '__main__':
    keyboard.go()