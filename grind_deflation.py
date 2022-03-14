from findwindow import *
from utils import *
from time import sleep
from pyautogui import moveTo, press, click
from pyautogui import leftClick
import pyautogui
import pydirectinput
from place import *

ninja1 = Tower("ninja", 612, 399)
ninja2 = Tower("ninja", 667, 406)
ninja3 = Tower("ninja", 728, 407)
alch1 = Tower("alch", 675, 357)
sniper1 = Tower("sniper", 1216, 504)
glue1 = Tower("glue", 430, 400)
obyn = Tower("hero", 790, 404)


def game():

    ninja1.place(upgrade=[4, 0, 2])
    ninja2.place(upgrade=[4, 0, 2])
    ninja3.place(upgrade=[4, 0, 2])
    alch1.place(upgrade=[4, 0, 1])
    glue1.place(upgrade=[2, 1, 0])
    obyn.place()
    sniper1.place(targeting=3)
    Game.game_play()


if __name__ == "__main__":
    to_front()
    dark_castle = Game("dark castle", "deflation", 360)
    loop = 1
    while loop < 100:
        print("repeated times: " + str(loop))
        dark_castle.ready()
        game()
        dark_castle.check_upgrade()
        dark_castle.game_exit()
        loop += 1
