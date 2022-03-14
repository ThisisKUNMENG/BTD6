
from findwindow import *
from utils import *
from time import sleep
from pyautogui import moveTo, click
import pyautogui
from pydirectinput import press
import json

with open("hotkeys.json", 'r') as f:
    hotkey = json.load(f)


class Tower:
    def __init__(self, name, x, y):
        if name not in hotkey:
            sys.exit(300)
        self.name = name
        self.x = left + x
        self.y = top + y

    def place(self, **kwargs):
        sleep(0.1)
        press(hotkey[self.name])
        sleep(0.3)
        moveTo(self.x, self.y)
        sleep(0.3)
        click()
        sleep(0.1)
        if "upgrade" in kwargs.keys() or "targeting" in kwargs.keys():
            click()
            sleep(0.1)
            if "upgrade" in kwargs.keys():
                self._upgrade(kwargs["upgrade"][0], kwargs["upgrade"][1], kwargs["upgrade"][2])
            if "targeting" in kwargs.keys():
                self.targeting(kwargs["targeting"])
            click()
            sleep(0.1)

    def upgrade_to(self, path1=0, path2=0, path3=0):
        sleep(0.1)
        moveTo(self.x, self.y)
        sleep(0.1)
        click()
        sleep(0.1)
        self._upgrade(path1, path2, path3)
        click()
        sleep(0.1)

    def sell(self):
        sleep(0.1)
        moveTo(self.x, self.y)
        sleep(0.1)
        click()
        sleep(0.1)
        press(hotkey["sell"])
        sleep(0.1)

    @staticmethod
    def targeting(to):
        sleep(0.1)
        while to != 0:
            press(hotkey["target"])
            sleep(0.05)
            to -= 1

    @staticmethod
    def _upgrade(path1, path2, path3):
        while path1 != 0:
            press(hotkey["path1"])
            sleep(0.05)
            path1 -= 1
        while path2 != 0:
            press(hotkey["path2"])
            sleep(0.05)
            path2 -= 1
        while path3 != 0:
            press(hotkey["path3"])
            sleep(0.05)
            path3 -= 1

