from findwindow import *
from utils import *
from time import sleep
from pyautogui import moveTo, press, click
from pyautogui import leftClick
import pyautogui
import pydirectinput
from PIL.ImageGrab import grab
import json


if __name__ == '__main__':
    x = 1354 + left
    y = 680 + top
    moveTo(x, y)
    c = grab().load()[x, y]
    print(c)


# (34, 148, 0)
# (34, 147, 0)
