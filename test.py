import easyocr
import json
from BTD6_Automation import *
from PIL.ImageGrab import grab
import numpy as np
import pytesseract

# reader = easyocr.Reader(['en'], gpu = False)


def dark_castle_deflation():
    ninja1 = Tower("ninja", 612, 399)
    ninja2 = Tower("ninja", 667, 406)
    ninja3 = Tower("ninja", 728, 407)
    alch1 = Tower("alch", 675, 357)
    sniper1 = Tower("sniper", 1216, 504)
    glue1 = Tower("glue", 430, 400)
    obyn = Tower("hero", 790, 404)
    Game.game_play()
    obyn.place()
    ninja1.place(upgrade=[4, 0, 2])
    ninja2.place(upgrade=[4, 0, 2])
    ninja3.place(upgrade=[4, 0, 2])
    alch1.place(upgrade=[4, 0, 1])
    glue1.place(upgrade=[2, 1, 0])
    sniper1.place(targeting=3)



if __name__ == '__main__':
    to_front()
    a = BlackBoarder("dark castle", dark_castle_deflation)
    a.run()


