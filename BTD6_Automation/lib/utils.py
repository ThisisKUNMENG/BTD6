from typing import Callable

import numpy as np
import easyocr
from PIL import ImageOps

from .entry_point import *
from .dicts import *

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


def _game_check(b1: bool, b2: bool) -> bool:
    """
    check whether the game is lost, victory, or level upgrade.
    """
    text = []
    upgrade = grab(701, 482, 825, 526)
    upgrade1 = reader.readtext(np.array(upgrade))
    if upgrade1:
        if upgrade1[0][1] == "Level" or upgrade1[0][1] == "LeveL":
            logger.info("Upgrade!")
            click()
            click()
    if b1:
        p1 = grab(715, 547, 903, 568)
        p11 = reader.readtext(np.array(p1), blocklist="X0123456789")
        if p11:
            text.append(p11)
    if b2:
        p2 = grab(640, 573, 957, 616)
        p22 = reader.readtext(np.array(p2), blocklist="X0123456789")
        if p22:
            text.append(p22)
    if not text:
        return True
    t = []
    for i in text:
        for j in i:
            t.append(j[1].lower())
    logger.debug("check found: %s", ",".join(t))
    for k in t:
        if k == "bloons leaked":
            logger.warning("lost")
            raise GameError("lost")
        if k == "generated":
            logger.info("victory")
            # raise GameError("victory")
            return False
        if "insta" in k:
            click()
            logger.info("insta monkey!")
            click()
    return True


def check(lose: bool = True, victory: bool = True) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Callable:
            global check_for_insta
            _game_check(lose | victory, check_for_insta)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def to_front() -> None:
    logger.info("letting the BTD6 window be at front")
    move_to(400, 400)
    click(wait=0.1)
    click()


def _to_map(m: dict) -> None:
    logger.info("entering the map %s", m["name"])
    page = m["page"] - 1
    # to level
    if m["level"] == "expert":
        move_to(1111, 850)
        click(wait=2)
    elif m["level"] == "advanced":
        move_to(900, 850)
        click(wait=2)
    elif m["level"] == "intermediate":
        move_to(700, 850)
        click(wait=2)
    elif m["level"] == "beginner":
        move_to(480, 850)
        sleep(0.2)
    else:
        sys.exit(303)
    # to page
    while page != 0:
        click(wait=2)
        page -= 1
    # get in map
    move_to(pos_loc[m["pos"] - 1][0], pos_loc[m["pos"] - 1][1], wait=2)
    click(wait=1)


def _to_mode(mode: str) -> None:
    logger.debug("entering the mode %s", modes[mode]["difficulty"])
    if modes[mode]["difficulty"] == "easy":
        move_to(530, 390, wait=2)
        click(wait=1)
    elif modes[mode]["difficulty"] == "medium":
        move_to(800, 390, wait=2)
        click(wait=1)
    elif modes[mode]["difficulty"] == "hard" or modes[mode]["difficulty"] == "impoppable":
        move_to(1075, 390, wait=2)
        click(wait=1)
    move_to(modes[mode]["cord"][0], modes[mode]["cord"][1], wait=2)
    click(wait=9)
    click(wait=5)


class Game:
    def __init__(self, m: str, mode: str):
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
    def game_play() -> None:
        logger.info("game starts")
        sleep(0.1)
        press("space")
        press("space")

    def game_exit(self) -> None:
        self._vic()
        self._to_home()

    @staticmethod
    def _vic() -> None:
        global check_for_insta
        while _game_check(True, check_for_insta):
            pass
        move_to(400, 400, wait=2)
        click(wait=5)
        move_to(800, 800, wait=0.5)
        click(wait=5)

    @staticmethod
    def _to_home() -> None:
        move_to(580, 733, wait=0.5)
        click(wait=2)
        click(wait=15)

    def free_play(self) -> None:
        self._vic()
        self._to_free()
        global check_for_insta
        check_for_insta = True

    @staticmethod
    def _to_free() -> None:
        move_to(1025, 733, wait=0.5)
        click(wait=2)
        click(wait=2)

    @staticmethod
    def play() -> None:
        sleep(5)
        move_to(700, 850)
        click(wait=4)

    def to_map(self) -> None:
        _to_map(self.map)
        sleep(1)

    def to_mode(self) -> None:
        _to_mode(self.mode)

    def ready(self) -> None:
        sleep(5)
        if collection_event:
            if check_need_collect():
                move_to(807, 606)
                click(wait=2)
                collect()
        self.play()
        self.to_map()
        self.to_mode()

    @staticmethod
    def lose_home() -> None:
        move_to(600, 700, wait=0.5)
        click(wait=4)

    @staticmethod
    def lose_restart() -> None:
        # TODO to be finished
        move_to(800, 700, wait=0.5)
        click(wait=4)


@check()
def get_money() -> int:
    money_pos = [305, 48, 400, 83]
    c = grab(money_pos)
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

def check_need_collect() -> bool:
    x1, x2 = 614, 852
    y1, y2 = 57, 113
    p = grab(x1, y1, x2, y2)
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
    move_to(250, 250)
    click()
    for i in range(5):
        move_to(555 + 125 * i, 470)
        click(wait=1)
        click(wait=1)
    sleep(0.5)
    click(wait=1)
    move_to(61, 73)
    click(wait=1)