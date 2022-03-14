import sys
from findwindow import *
from utils import *
from time import sleep
from pyautogui import moveTo, click
import pyautogui
from pydirectinput import press
import json
from PIL.ImageGrab import grab

with open("hotkeys.json", 'r') as f:
    hotkey = json.load(f)


def check_for_upgrade(path, lr):
    y = 0
    x = 0
    if lr == "l":
        x = 337
    elif lr == "r":
        x = 1354
    else:
        sys.exit(311)
    if path == 1:
        y = 450
    elif path == 2:
        y = 560
    elif path == 3:
        y = 680
    else:
        sys.exit(312)
    color = grab().load()[left+x, top+y]
    if color[2] > 80:
        return True
    elif color[2] < 50:
        return False
    else:
        sys.exit(310)


class Tower:
    def __init__(self, name, x, y):
        if name not in hotkey:
            sys.exit(300)
        self.name = name
        self.x = left + x
        self.y = top + y
        if x >= 697:
            self.lr = "l"
        else:
            self.lr = "r"

    def place(self, **kwargs):
        sleep(0.1)
        press(hotkey[self.name])
        sleep(0.3)
        moveTo(self.x, self.y)
        sleep(0.3)
        click()
        sleep(0.2)
        if "upgrade" in kwargs.keys() or "targeting" in kwargs.keys():
            click()
            sleep(0.1)
            if "upgrade" in kwargs.keys():
                self._upgrade(kwargs["upgrade"][0], kwargs["upgrade"][1], kwargs["upgrade"][2])
            if "targeting" in kwargs.keys():
                self.targeting(kwargs["targeting"])
            click()
            sleep(0.3)

    def upgrade_to(self, path1=0, path2=0, path3=0):
        sleep(0.1)
        moveTo(self.x, self.y)
        sleep(0.1)
        click()
        sleep(0.1)
        self._upgrade(path1, path2, path3)
        click()
        sleep(0.1)

    def place_when(self, tower, path):
        sleep(0.1)
        moveTo(tower.x, tower.y)
        sleep(0.1)
        click()
        sleep(0.1)
        while check_for_upgrade(path, tower.lr):
            sleep(5)
        click()
        sleep(0.1)
        self.place()
        sleep(0.1)

    def upgrade_with_order(self, order):
        sleep(0.1)
        moveTo(self.x, self.y)
        sleep(0.1)
        click()
        sleep(0.1)
        for i in order:
            sleep(0.3)
            if i == 1:
                self._upgrade(1, 0, 0)
            if i == 2:
                self._upgrade(0, 1, 0)
            if i == 3:
                self._upgrade(0, 0, 1)
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

    def change_targeting(self, to):
        sleep(0.1)
        moveTo(self.x, self.y)
        sleep(0.1)
        click()
        sleep(0.1)
        while to != 0:
            press(hotkey["target"])
            sleep(0.05)
            to -= 1
        click()
        sleep(0.1)

    def _upgrade(self, path1, path2, path3):
        while path1 != 0:
            while check_for_upgrade(1, self.lr):
                sleep(5)
            press(hotkey["path1"])
            sleep(0.05)
            path1 -= 1
        while path2 != 0:
            while check_for_upgrade(2, self.lr):
                sleep(5)
            press(hotkey["path2"])
            sleep(0.05)
            path2 -= 1
        while path3 != 0:
            while check_for_upgrade(3, self.lr):
                sleep(5)
            press(hotkey["path3"])
            sleep(0.05)
            path3 -= 1

