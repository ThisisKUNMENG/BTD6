import sys

from .findwindow import *
from .dicts import *
from time import sleep
from pyautogui import moveTo, click
from pydirectinput import press
from PIL.ImageGrab import grab
import json
import numpy as np
import easyocr

__all__ = ["tower_money", "to_front", "Game", "get_money", "LoseError", "check_lose"]

reader = easyocr.Reader(['en'], gpu = False)

tower_money = {}


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
    elif m["level"] == "advanced":
        moveTo(left + 900, top + 850)
        sleep(0.2)
        click()
        sleep(2)
    elif m["level"] == "intermediate":
        moveTo(left + 700, top + 850)
        sleep(0.2)
        click()
        sleep(2)
    elif m["level"] == "beginner":
        moveTo(left + 480, top + 850)
        sleep(0.2)
        click()
        sleep(2)
    else:
        sys.exit(303)
    # to page
    while page != 0:
        click()
        sleep(2)
        page -= 1
    # get in map
    moveTo(left + pos_loc[m["pos"]-1][0], top + pos_loc[m["pos"]-1][1])
    sleep(2)
    click()
    sleep(1)


def _to_mode(mode):
    if modes[mode]["difficulty"] == "easy":
        moveTo(left + 530, top + 390)
        sleep(2)
        click()
        sleep(1)
    elif modes[mode]["difficulty"] == "medium":
        moveTo(left + 800, top + 390)
        sleep(2)
        click()
        sleep(1)
    elif modes[mode]["difficulty"] == "hard" or modes[mode]["difficulty"] == "impoppable":
        moveTo(left + 1075, top + 390)
        sleep(2)
        click()
        sleep(1)
    moveTo(left + modes[mode]["cord"][0], top + modes[mode]["cord"][1])
    sleep(2)
    click()
    sleep(9)
    click()
    sleep(5)


class Game:
    def __init__(self, m, mode):
        self._t = 380
        if m not in maps:
            sys.exit(301)
        if mode not in modes:
            sys.exit(302)
        self.map = maps[m]
        self.mode = mode
        self.difficulty = modes[mode]["difficulty"]
        for i in tower_money_all:
            tower_money[i] = tower_money_all[i][self.difficulty]
        print(tower_money)

    @staticmethod
    def game_play():
        sleep(0.1)
        press("space")
        sleep(0.1)
        press("space")
        sleep(0.1)

    @property
    def wait_time(self):
        return self._t

    @wait_time.setter
    def wait_time(self, value):
        self._t = value

    @wait_time.deleter
    def wait_time(self):
        del self._t

    def game_exit(self):
        self._vic()
        self._to_home()

    @staticmethod
    def _vic():
        moveTo(left + 400, top + 400)
        sleep(2)
        click()
        sleep(5)
        moveTo(left+800, top+800)
        sleep(0.5)
        click()
        sleep(5)

    @staticmethod
    def _to_home():
        moveTo(left+580, top+733)
        sleep(0.5)
        click()
        sleep(2)
        click()
        sleep(4)

    def free_play(self):
        self._vic()
        self._to_free()

    @staticmethod
    def _to_free():
        moveTo(left+1025, top+733)
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

    @staticmethod
    def lose_home():
        moveTo(left+600, top+700)
        sleep(0.5)
        click()
        sleep(4)

    @staticmethod
    def lose_restart():
        moveTo(left+800, top+700)
        sleep(0.5)
        click()
        sleep(4)

    def check_upgrade(self):
        sleep(0.1)
        moveTo(left+510, top+672)
        wait_time = self._t
        while wait_time > 0:
            print("supposed game time remaining: " + str(wait_time) + " seconds")
            sleep(5)
            check_lose()
            sleep(5)
            click()
            sleep(0.1)
            click()
            press("space")
            sleep(0.05)
            press("space")
            sleep(0.05)
            wait_time -= 10


def get_money():
    c = grab(money)
    im = np.array(c)
    text = reader.readtext(im, allowlist="0123456789", detail=0)
    m = 0
    try:
        m = int(text[0])
    except Exception as e:
        print("error ", text)
        # sys.exit(400)
    print("money:", m)
    return m


class LoseError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


def check_lose():
    p = grab([left+603, top+268, left+1020, top+380])
    text = reader.readtext(np.array(p), allowlist='DEeFAT', detail=0)
    print(text)
    if 'DEFED' in text or 'DEFEAT' in text or 'DEEEE' in text or 'DEEE' in text:
        raise LoseError("lost")
    else:
        return False


def check_victory():
    p = grab([left+574, top+122, left+1014, top+231])
    text = reader.readtext(np.array(p), allowlist='VICTORY', detail=0)
    if 'VICTORY' in text:
        return True
    else:
        return False
