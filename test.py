import easyocr
import json
from BTD6_Automation import *
from PIL.ImageGrab import grab
import numpy as np
import pytesseract

# reader = easyocr.Reader(['en'], gpu = False)
with open("BTD6_Automation/lib/tower_money.json", 'r') as f:
    tower_money = json.load(f)

i = {}
reader = easyocr.Reader(['en'], gpu = False)

if __name__ == '__main__':
    p = grab([603, 268, 1015, 380])
    print(1)
    # p = grab([574, 122, 1014, 231])
    # text = reader.readtext(np.array(p), allowlist='VICTORY', detail=0)
    text = reader.readtext(np.array(p), allowlist='DEeFAT', detail=0)
    print(2)
    print(text)

    if 'DEFED' in text or 'DEFEAT' in text or 'DEEEE' in text:
        raise LoseError("lost")


# (34, 148, 0)
# (34, 147, 0)
