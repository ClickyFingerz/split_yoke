print("Starting")

### TO DO ###
# - Momentary swap sides

import board

from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.combos import Combos, Chord, Sequence
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.oneshot import OneShot
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.tapdance import TapDance
from kmk.scanners import DiodeOrientation

#
### KEYBOARD ###
keyboard = KMKKeyboard()
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.col_pins = (board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9)
keyboard.row_pins = (board.GP4, board.GP5, board.GP6, board.GP7, board.GP8)

# Comment one of these for each side
split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT

uart_flip = False if split_side == SplitSide.LEFT else True

split = Split(
    #split_side=split_side,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type = SplitType.UART,  # Defaults to UART
    split_target_left = True,  # Assumes that left will be the one on USB. Set to False if it will be the right
    #uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin = board.GP1,
    data_pin2 = board.GP0,
    uart_flip = uart_flip,  # Reverses the RX and TX pins if both are provided -- works with LEFT=True RIGHT=False
    use_pio = True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)

keyboard.debug_enabled = True
print("Debugging...")

holdtap = HoldTap()
holdtap.prefer_hold = False
holdtap.repeat = HoldTapRepeat
holdtap.tap_time=250

### MODULES ###
combos = Combos()
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(combos)
keyboard.modules.append(holdtap)
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(OneShot())
keyboard.modules.append(split)
keyboard.modules.append(TapDance())

keyboard.coord_mapping = [
     1,  2,  3,  4,  5,  30, 31, 32, 33, 34,
 6,  7,  8,  9, 10, 11,  36, 37, 38, 39, 40, 41,
12, 13, 14, 15, 16, 17,  42, 43, 44, 45, 46, 47,
            21, 22, 23,  48, 49, 50,
    25, 26, 27, 28, 29,  54, 55, 56, 57, 58,
]

### KEYMAP ###
# 
# To do:
#   - Dynamic sequence recording
#   - Assign right hand extra key
#   - Window snap to quadrant
#

DEL_WORD = simple_key_sequence((KC.LCTL(KC.LSFT(KC.LEFT)), KC.BSPC))
DOWN_CTL = KC.HT(KC.DOWN, KC.LCTL)
LEFT_ALT = KC.HT(KC.LEFT, KC.LALT)
OS_LSFT  = KC.OS(KC.LSFT)
OS_SYM   = KC.OS(KC.MO(2))
R_LALT   = KC.HT(KC.R, KC.LALT)
RGHT_SFT = KC.HT(KC.RIGHT, KC.LSFT)
S_LCTL   = KC.HT(KC.S, KC.LCTL)
T_LSFT   = KC.HT(KC.T, KC.LSFT)
THE      = send_string("the")
YOU      = send_string("you")

# Layers
NUM_SPC  = KC.LT(1,KC.SPC)
SYM      = KC.MO(2)
NAV_BSPC = KC.LT(3,KC.BSPC,repeat=HoldTapRepeat.TAP) 
CODE     = KC.MO(4)
LEFTY    = KC.MO(5)

# Visual Studio
DBG_BLD  = KC.LCTL(KC.LSFT(KC.B))
DBG_BKPT = KC.F9
DBG_INTO = KC.F11
DBG_OVER = KC.F10
DBG_OUT  = KC.LSFT(KC.F11)
DBG_RST  = KC.LCTL(KC.LSFT(KC.F5))
DBG_RUN  = KC.LCTL(KC.F5)
DBG_STOP = KC.LSFT(KC.F5)
DBG_STRT = KC.F5
MOV_DOWN = KC.LALT(KC.DOWN)
MOV_UP   = KC.LALT(KC.UP)
REFACTOR = KC.LALT(KC.ENT)

### COMBOS ###
combos.combos = [
    Chord((KC.Q, KC.W), KC.GRV),
    Chord((KC.W, KC.F), KC.ESC),
    Chord((KC.C, KC.X), KC.SPC),
    Chord((KC.Q, KC.W, KC.F, KC.P), KC.RELOAD)
]

keyboard.keymap = [

    # [0] COLEMAK
    [
    #       GP14        GP13        GP12        GP11        GP10        GP9      ||     GP14        GP13        GP12        GP11        GP10        GP9
                        KC.Q,       KC.W,       KC.F,       KC.P,       KC.B,           KC.J,       KC.L,       KC.U,       KC.Y,       KC.QUOT,               # GP4
            KC.TAB,     KC.A,       KC.R,       KC.S,       KC.T  ,     KC.G,           KC.M,       KC.N,       KC.E,       KC.I,       KC.O,       KC.MINS,   # GP5
            KC.LCTL,    KC.Z,       KC.X,       KC.C,       KC.D,       KC.V,           KC.K,       KC.H,       KC.COMM,    KC.DOT,     KC.SLSH,    KC.ENT,    # GP6
                                                THE,        NAV_BSPC,   OS_LSFT,        OS_SYM,     NUM_SPC,    YOU,                                           # GP7
                        KC.BSPC,    KC.ENT,     KC.DEL,     LEFTY,      KC.TRNS,        KC.LCTL,    KC.LALT,    KC.LGUI,    CODE,       KC.TRNS                # GP8
    #                   UP          FORWARD     DOWN        BACK        CLICK           DOWN        FORWARD     UP          BACK        CLICK
    ],

    # [1] NUMBER
    [
    #       GP14        GP13        GP12        GP11        GP10        GP9      ||     GP14        GP13        GP12        GP11        GP10        GP9
                        KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,        KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.F9,      KC.F10,                # GP4
            KC.PLUS,    KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,          KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINS,   # GP5
            KC.LCTL,    KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,          KC.F6,      KC.F7,      KC.F8,      KC.DOT,     KC.SLSH,    KC.EQL,    # GP6
                                                KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,                                       # GP7
                        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS                # GP8
    #                   UP          FORWARD     DOWN        BACK        CLICK           DOWN        FORWARD     UP          BACK        CLICK
    ],

    # [2] SYMBOL
    [
    #       GP14        GP13        GP12        GP11        GP10        GP9      ||     GP14        GP13        GP12        GP11        GP10        GP9
                        KC.GRV,     KC.AT,      KC.PIPE,    KC.DLR,     KC.CIRC,        KC.CIRC,    KC.DLR,     KC.PIPE,    KC.AT,      KC.TILDE,              # GP4
            KC.AMPR,    KC.PERC,    KC.COLN,    KC.EXLM,    KC.HASH,    KC.BSLS,        KC.BSLS,    KC.HASH,    KC.EXLM,    KC.COLN,    KC.PERC,    KC.AMPR,   # GP5
            KC.TILD,    KC.SCLN,    KC.LBRC,    KC.LCBR,    KC.LPRN,    KC.ASTR,        KC.ASTR,    KC.RPRN,    KC.RCBR,    KC.RBRC,    KC.SCLN,    KC.TILD,   # GP6
                                                KC.TRNS,    DEL_WORD,   KC.TRNS,        KC.TO(0),   KC.TRNS,    KC.TRNS,                                       # GP7
                        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.RLD,     KC.TRNS                # GP8
    #                   UP          FORWARD     DOWN        BACK        CLICK           DOWN        FORWARD     UP          BACK        CLICK
    ],
    
    # [3] NAV
    [
    #       GP14        GP13        GP12        GP11        GP10        GP9      ||     GP14        GP13        GP12        GP11        GP10        GP9
                        KC.TRNS,    KC.TRNS,    KC.UP,      KC.MPLY,    KC.TRNS,        KC.TRNS,    KC.HOME,    KC.UP,      KC.END,     KC.TRNS,               # GP4
            KC.TRNS,    KC.TRNS,    LEFT_ALT,   DOWN_CTL,   RGHT_SFT,   KC.TRNS,        KC.PGUP,    KC.LEFT,    KC.DOWN,    KC.RGHT,    KC.BSPC,    KC.TRNS,   # GP5
            KC.TRNS,    KC.MPRV,    KC.MNXT,    KC.VOLD,    KC.VOLU,    KC.TRNS,        KC.PGDN,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.DEL,     KC.TRNS,   # GP6
                                                KC.MUTE,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,                                       # GP7
                        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS                # GP8
    #                   UP          FORWARD     DOWN        BACK        CLICK           DOWN        FORWARD     UP          BACK        CLICK
    ],

    # [4] CODE (VISUAL STUDIO)
    [
    #       GP14        GP13        GP12        GP11        GP10        GP9      ||     GP14        GP13        GP12        GP11        GP10        GP9
                        KC.TRNS,    KC.TRNS,    DBG_OUT,    MOV_UP,     DBG_BLD,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,               # GP4
            KC.TRNS,    DBG_RST,    DBG_STOP,   DBG_STRT,   REFACTOR,   DBG_OVER,       KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,   # GP5
            KC.TRNS,    KC.TRNS,    KC.TRNS,    DBG_INTO,   MOV_DOWN,   KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,   # GP6
                                                DBG_BKPT,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,                                       # GP7
                        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS                # GP8
    #                   UP          FORWARD     DOWN        BACK        CLICK           DOWN        FORWARD     UP          BACK        CLICK
    ],

    # [5] LEFTY
    [
    #       GP14        GP13        GP12        GP11        GP10        GP9      ||     GP14        GP13        GP12        GP11        GP10        GP9
                        KC.QUOT,    KC.Y,       KC.U,       KC.L,       KC.J,           KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,               # GP4
            KC.MINS,    KC.O,       KC.I,       KC.E,       KC.N,       KC.M,           KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,   # GP5
            KC.TRNS,    KC.SLSH,    KC.DOT,     KC.COMM,    KC.H,       KC.K,           KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,   # GP6
                                                KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,                                       # GP7
                        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS                # GP8
    #                   UP          FORWARD     DOWN        BACK        CLICK           DOWN        FORWARD     UP          BACK        CLICK
    ],

    # [x] TEMPLATE
    #[
    #       GP14        GP13        GP12        GP11        GP10        GP9      ||     GP14        GP13        GP12        GP11        GP10        GP9
    #                    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,               # GP4
    #        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,   # GP5
    #        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,   # GP6
    #                                            KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,                                       # GP7
    #                    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,        KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS                # GP8
    #                   UP          FORWARD     DOWN        BACK        CLICK           DOWN        FORWARD     UP          BACK        CLICK
    #],
]

if __name__ == '__main__':
    keyboard.go()
