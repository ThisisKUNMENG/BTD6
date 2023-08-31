import sys
from .findwindow import *
from .dicts import *
from time import sleep, time
from pyautogui import moveTo, click
from pydirectinput import press
from PIL.ImageGrab import grab
import numpy as np
import easyocr
from PIL import ImageOps
import json

# __all__ = ["tower_money", "to_front", "Game", "get_money", "GameError", "check"]

reader = easyocr.Reader(['en'])

tower_money = {}

check_for_insta = False
collection_event = True


# def check_lose():
#     p = grab([left+715, top+517, left+903, top+548])
#     text = reader.readtext(np.array(p), detail=0)
#     logger.debug("check lose found: %s", ",".join(text))
#     if 'Bloons Leaked' in text:
#         raise GameError("lost")
#     # if it is "Generated", it is victory.
#     else:
#         return False
#
#
# def check_victory():
#     p = grab([left+574, top+122, left+1014, top+231])
#     text = reader.readtext(np.array(p), allowlist='VICTORY', detail=0)
#     logger.debug("check victory found: %s", ",".join(text))
#     if 'VICTORY' in text:
#         raise GameError("victory")
#     else:
#         return False
#
#
# def check_insta():
#     p = grab([left+640, top+573, left+957, top+616])
#     text = reader.readtext(np.array(p))
#     logger.debug("check insta found: %s", ",".join(text))
#     t = []
#     for i in text:
#         t.append(i[1])
#     if 'InSTA-Monkey' in t or "InSTA-Monkev" in t:
#         click()
#     else:
#         return False
#     pass


def _game_check(b1, b2):
    """
    check whether the game is lost, victory, or level upgrade.
    """
    text = []
    upgrade = grab([left+701, top+482, left+825, top+526])
    upgrade1 = reader.readtext(np.array(upgrade))
    if upgrade1:
        if upgrade1[0][1] == "Level" or upgrade1[0][1] == "LeveL":
            logger.info("Upgrade!")
            click()
            sleep(0.6)
            click()
            sleep(0.5)
    if b1:
        p1 = grab([left+715, top+547, left+903, top+568])
        p11 = reader.readtext(np.array(p1), blocklist="X0123456789")
        if p11:
            text.append(p11)
    if b2:
        p2 = grab([left + 640, top + 573, left + 957, top + 616])
        p22 = reader.readtext(np.array(p2), blocklist="X0123456789")
        if p22:
            text.append(p22)
    if not text:
        return True
    t = []
    for i in text:
        for j in i:
            t.append(j[1])
    logger.debug("check found: %s", ",".join(t))
    for k in t:
        if k == "Bloons Leaked":
            logger.warning("lost")
            raise GameError("lost")
        if k == "Generated":
            logger.info("victory")
            # raise GameError("victory")
            return False
        if "InSTA" in k:
            click()
            logger.info("insta monkey!")
    return True


def check(lose=True, victory=True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            global check_for_insta
            _game_check(lose | victory, check_for_insta)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def to_front():
    logger.info("letting the BTD6 window be at front")
    moveTo(left+400, top+400)
    sleep(0.1)
    click()
    sleep(0.1)
    click()
    sleep(0.5)


def _to_map(m):
    logger.info("entering the map %s", m["name"])
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
        # click()
        # sleep(2)
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
    logger.debug("entering the mode %s", modes[mode]["difficulty"])
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
        if m not in maps:
            sys.exit(301)
        if mode not in modes:
            sys.exit(302)
        self.map = maps[m]
        self.mode = mode
        self.difficulty = modes[mode]["difficulty"]
        if self.difficulty == "impoppable" or self.difficulty == "chimps":
            global check_for_insta
            check_for_insta = True
        for i in tower_money_all:
            tower_money[i] = tower_money_all[i][self.difficulty]

    @staticmethod
    def game_play():
        logger.info("game starts")
        sleep(0.1)
        press("space")
        sleep(0.1)
        press("space")
        sleep(0.1)

    def game_exit(self):
        self._vic()
        self._to_home()

    @staticmethod
    def _vic():
        global check_for_insta
        while _game_check(True, check_for_insta):
            pass
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
        global check_for_insta
        check_for_insta = True

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
        sleep(5)
        if collection_event:
            if check_need_collect():
                moveTo(807, 606)
                sleep(0.1)
                click()
                sleep(2)
                collect()
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
        # TODO to be finished
        moveTo(left+800, top+700)
        sleep(0.5)
        click()
        sleep(4)


@check()
def get_money():
    c = grab(money)
    c = ImageOps.grayscale(c)
    im = np.array(c)
    text = reader.readtext(im, allowlist="0123456789,", detail=0)
    m = 0
    try:
        m = int(text[0].replace(",", ""))
    except Exception as e:
        logger.warning("get money error ", text)
    logger.debug("current money: %d", m)
    return m


class GameError(RuntimeError):
    def __init__(self, arg):
        self.args = arg
        logger.warning("There is something wrong")

def check_need_collect():
    x1, x2 = 614, 852
    y1, y2 = 57, 113
    p = grab([left+x1, top+y1, left+x2, top+y2])
    read = reader.readtext(np.array(p), blocklist="X0123456789", detail=0)
    if read:
        read_word = read[0].lower()
    else:
        read_word = ""
    if read_word == "collection":
        logger.info("need to collect!")
        return True
    else:
        return False


def collect():
    moveTo(left + 250, top + 250)
    sleep(0.2)
    click()
    for i in range(5):
        moveTo(left+555+125*i, top+470)
        sleep(0.1)
        click()
        sleep(1)
        click()
        sleep(1)
    sleep(0.5)
    click()
    sleep(1)
    moveTo(61, 73)
    sleep(0.1)
    click()
    sleep(1)