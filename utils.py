from findwindow import *
from time import sleep
from pyautogui import moveTo, click
import pyautogui
from pydirectinput import press
from PIL.ImageGrab import grab
import json

with open("maps.json", 'r') as f:
    maps = json.load(f)

modes = ["deflation", "easy standard"]


def to_front():
    moveTo(left+400, top+400)
    sleep(0.1)
    click()
    sleep(0.1)
    click()
    sleep(0.5)


def _to_map(m):
    page = m["page"] - 1
    # to level
    if m["level"] == "expert":
        moveTo(left + 1111, top + 850)
        sleep(0.2)
        click()
        sleep(2)
    # to page
    while page != 0:
        click()
        sleep(2)
        page -= 1
    # get in map
    if m["pos"] == 2:
        moveTo(left + 813, top + 238)
        sleep(2)
        click()
        sleep(1)


def _to_mode(mode):
    if mode == "deflation":
        moveTo(left + 530, top + 390)
        sleep(2)
        click()
        sleep(1)
        moveTo(left + 1077, top + 416)
        sleep(2)
        click()
        sleep(9)
        click()
        sleep(5)


class Game:
    def __init__(self, m, mode, t):
        self.t = t
        if m not in maps:
            sys.exit(301)
        if mode not in modes:
            sys.exit(302)
        self.map = maps[m]
        self.mode = mode

    @staticmethod
    def game_play():
        sleep(0.1)
        press("space")
        sleep(0.1)
        press("space")
        sleep(0.1)

    @staticmethod
    def game_exit():
        sleep(2)
        click()
        sleep(0.5)
        moveTo(left+800, top+800)
        sleep(0.5)
        click()
        sleep(3)
        moveTo(left+580, top+733)
        sleep(0.5)
        click()
        sleep(2)
        click()
        sleep(2)

    @staticmethod
    def play():
        sleep(5)
        moveTo(left+700, top+850)
        sleep(0.5)
        click()
        sleep(4)

    def to_map(self):
        _to_map(self.map)
        sleep(1)

    def to_mode(self):
        _to_mode(self.mode)

    def ready(self):
        self.play()
        self.to_map()
        self.to_mode()

    def check_upgrade(self):
        sleep(0.1)
        moveTo(left+510, top+672)
        tt = self.t
        while tt > 0:
            print("supposed game time remaining: " + str(tt) + " seconds")
            sleep(10)
            click()
            sleep(0.1)
            click()
            press("space")
            sleep(0.05)
            press("space")
            sleep(0.05)
            tt -= 10


