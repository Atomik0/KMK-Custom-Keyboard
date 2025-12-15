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

RALT = ModifierKey(64)
ISO_LTGT = KeyboardKey(100)

TOKEN_MAP = {
    "RALT": RALT,
    "ISO_LTGT": ISO_LTGT,
}

def _parse_key(token: str):
    """
    Soporta:
    - KC.X (ej: "KC.A", "KC.ENT")
    - MO(n) (ej: "MO(1)")
    - Tokens especiales: "RALT", "ISO_LTGT"
    - "KC.NO" / "KC.TRNS" etc.
    """
    if token is None:
        return KC.NO

    token = str(token).strip()
    if token == "":
        return KC.NO
    
    if token in TOKEN_MAP:
        return TOKEN_MAP[token]
    
    if token.startswith("MO(") and token.endswith(")"):
        n_str = token[3:-1].strip()
        try:
            layer_num = int(n_str)
            return KC.MO(layer_num)
        except:
            return KC.NO
        
    if token.startswith("KC."):
        name = token[3:].strip()
        return getattr(KC, name, KC.NO)
    
    return KC.NO


def load_keymap_from_json(path="keymap.json"):
    try:
        import json
        with open(path, "r") as f:
            data = json.load(f)

        layers_data = data.get("layers", [])
        if not layers_data or not isinstance(layers_data, list):
            return None

        loaded = []
        for layer in layers_data:
            flat = []
            for row in layer:
                for token in row:
                    flat.append(_parse_key(token))
            loaded.append(flat)

        return loaded

    except Exception as e:
        print("ERROR loading keymap.json:", e)
        return None
    
def default_keymap():
    base = [KC.NO] * (6 * 14)
    base[0] = KC.A
    return [base]

km = load_keymap_from_json("keymap.json")
keyboard.keymap = km if km else default_keymap()

if __name__ == "__main__":
    keyboard.go()
