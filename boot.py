import board
from kmk.bootcfg import bootcfg

bootcfg(
    # COL2ROW
    sense = board.D0,  # col
    source = board.D1, # row
    boot_device = 0,
    cdc = False,
    consumer_control = True,
    keyboard = True,
    midi = False,
    mouse = True,
    nkro = False,
    pan = True,
    storage = True,
    usb_id = ("KMKeyboard", "Custom Wireless Split Ergo"),
)