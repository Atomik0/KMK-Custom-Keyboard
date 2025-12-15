import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, KeyboardKey, ModifierKey
from kmk.scanners import DiodeOrientation

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

keyboard.row_pins = (board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11)

keyboard.col_pins = (
    board.GP18, board.GP17, board.GP16, board.GP15, board.GP14, board.GP13, board.GP12,
    board.GP5,  board.GP4,  board.GP3,  board.GP2,  board.GP1,  board.GP0,  board.GP19
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

try:
    from kmk.modules.layers import Layers
except ImportError:
    from kmk.extensions.layers import Layers

layers = Layers()
keyboard.modules.append(layers)

FN = KC.MO(1)
RALT = ModifierKey(64)
XXXXXXX = KC.NO

ISO_LTGT = KeyboardKey(100)

keyboard.keymap = [
    [
        KC.ESC,  KC.F1,  KC.F2,  KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,  KC.F9,  KC.F10, KC.F11, KC.F12, KC.PSCR,    # --- FILA 0 (GP6)
        KC.GRV,  KC.N1,  KC.N2,  KC.N3,  KC.N4,  KC.N5,  KC.N6,  KC.N7,  KC.N8,  KC.N9,  KC.N0,  KC.MINS, KC.EQL, KC.BSPC,   # --- FILA 1 (GP7)
        KC.TAB,  ISO_LTGT, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC,                     # --- FILA 2 (GP8)
        KC.CAPS, KC.NO,  KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT,                     # --- FILA 3 (GP9)
        KC.LSFT, ISO_LTGT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.MINS, KC.RSFT, KC.NO,               # --- FILA 4 (GP10)
        KC.LCTL, KC.LGUI, KC.LALT, KC.NO, KC.NO, KC.NO, KC.SPC, KC.NO, KC.NO, KC.NO, RALT, FN, KC.RCTL, KC.NO,               # --- FILA 5 (GP11)
    ], [
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
    ],
]

if __name__ == "__main__":
    keyboard.go()
