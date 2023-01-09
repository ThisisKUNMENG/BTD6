# This module is to operate tower actions.

import sys
from .findwindow import *
from .utils import *
from .dicts import *
from time import sleep

from pyautogui import moveTo, click
from pydirectinput import press
from PIL.ImageGrab import grab


__all__ = ["Tower"]


@check()
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
        logger.warning("A problem in checking tower upgrade")
        return True


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
        if name != "hero":
            try:
                self.money = tower_money[name]
            except Exception as e:
                print("error", e)
        else:
            self.money = 0

    def place(self, **kwargs):
        sleep(0.1)
        if "money" in kwargs.keys():
            while get_money() < kwargs["money"]:
                sleep(3)
        else:
            while get_money() < self.money:
                sleep(3)
        logger.debug("placing %s at absolute position %d, %d", self.name, self.x, self.y)
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
                logger.debug("upgrade %s to [%d, %d, %d]", self.name,
                            kwargs["upgrade"][0], kwargs["upgrade"][1], kwargs["upgrade"][2])
                self._upgrade(kwargs["upgrade"][0], kwargs["upgrade"][1], kwargs["upgrade"][2])
            if "targeting" in kwargs.keys():
                logger.debug("change %s targeting by %d steps", self.name, kwargs["targeting"])
                self.targeting(kwargs["targeting"])
            click()
            sleep(0.3)

    def upgrade_to(self, path1=0, path2=0, path3=0):
        logger.debug("upgrade %s by [%d, %d, %d]", self.name, path1, path2, path3)
        sleep(0.1)
        moveTo(self.x, self.y)
        sleep(0.1)
        click()
        sleep(0.1)
        self._upgrade(path1, path2, path3)
        click()
        sleep(0.2)

    # def place_when(self, tower, path):
    #     sleep(0.1)
    #     moveTo(tower.x, tower.y)
    #     sleep(0.1)
    #     click()
    #     sleep(0.1)
    #     while check_for_upgrade(path, tower.lr):
    #         sleep(5)
    #     click()
    #     sleep(0.1)
    #     self.place()
    #     sleep(0.1)

    def place_money(self, amount, **kwargs):
        """
        a function to place tower when money is sufficient.
        NOTE: this is an outdated function, please use Tower.place(money=) to set money.

        :param amount: how much money that are needed to place the tower
        :param kwargs: upgrade or/and targeting
        """
        while get_money() < amount:
            sleep(3)
        if "upgrade" in kwargs.keys() and "targeting" in kwargs.keys():
            self.place(upgrade=kwargs["upgrade"], targeting=kwargs["targeting"])
        elif "upgrade" in kwargs.keys() and "targeting" not in kwargs.keys():
            self.place(upgrade=kwargs["upgrade"])
        elif "upgrade" not in kwargs.keys() and "targeting" in kwargs.keys():
            self.place(targeting=kwargs["targeting"])
        else:
            self.place()

    def upgrade_with_order(self, order):
        logger.debug(f"upgrade {self.name} with order {order}")
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
        logger.debug("sell %s", self.name)
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
        logger.debug("change %s targeting by %d steps", self.name, to)
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

