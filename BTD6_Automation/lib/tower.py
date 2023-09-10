"""
This module is to operate tower actions.
"""
from __future__ import annotations

from typing import Optional

from .utils import *
from .dicts import *


__all__ = ["Tower"]


class Tower:
    def __init__(self, name: str, x: int, y: int):
        if name not in hotkey:
            sys.exit(300)
        self.name = name
        self.x = x
        self.y = y
        if x >= 697:
            self.lr = "l"
        else:
            self.lr = "r"
        if name != "hero":
            try:
                self.money = tower_money[name]
            except Exception as e:
                print(name)
                print("error", e)
        else:
            self.money = 0

    def place(self,
              upgrade: Optional[list] = None,
              targeting: int = 0,
              money_t: int = 0):
        """
        place the tower at the chosen location.
            :param upgrade: upgrade the tower to [x, y, z], note this upgrade method only supports upgrading the tower
                from path 1 to path 3 in a sequence. Default is [0, 0, 0], which does not upgrade.
                If you want to upgrade in a specific order, use upgrade_with_order function.
            :param targeting: change targeting. Default is 0.
            :param money_t: If the tower money changes (for example military monkey's price reduction
                due to monkey knowledge), you can specify the money needed to place the tower.
            :return: self
        """
        if upgrade is None:
            upgrade = [0, 0, 0]
        sleep(0.1)
        if money_t != 0:
            self.money = money_t
        while get_money() < self.money:
            sleep(3)
        self._place()
        while self._check_place():
            # in case money check failed
            click()
            while get_money() < self.money:
                sleep(3)
            self._place()
        logger.debug("upgrade %s to [%d, %d, %d]", self.name, upgrade[0], upgrade[1], upgrade[2])
        self._upgrade(upgrade[0], upgrade[1], upgrade[2])
        logger.debug("change %s targeting by %d steps", self.name, targeting)
        self.targeting(targeting)
        click()
        return self

    def _place(self) -> None:
        logger.debug("placing %s at absolute position %d, %d", self.name, self.x, self.y)
        press(hotkey[self.name], wait=0.3)
        move_to(self.x, self.y)
        click(wait=0.2)
        click(wait=0.1)

    def _check_place(self) -> bool:
        """
            :return: True if the tower did not place
        """
        if self.lr == "l":
            pos = [[337, 450], [337, 560], [337, 680]]
        else:
            pos = [[1354, 450], [1354, 560], [1354, 680]]
        c1 = []
        c2 = []
        for pos_u in pos:
            c1.append(grab().load()[LEFT + pos_u[0], TOP + pos_u[1]])
        click(wait=0.1)
        for pos_u in pos:
            c2.append(grab().load()[LEFT + pos_u[0], TOP + pos_u[1]])
        if c1 == c2:
            logger.warning(f"Tower {self.name} is not placed!")
            return True
        else:
            click(wait=0.1)
            return False

    def upgrade_to(self, path1: int = 0, path2: int = 0, path3: int = 0):
        logger.debug("upgrade %s by [%d, %d, %d]", self.name, path1, path2, path3)
        sleep(0.1)
        move_to(self.x, self.y, wait=0.1)
        click(wait=0.1)
        self._upgrade(path1, path2, path3)
        click(wait=0.2)
        return self

    def place_money(self, amount: int, **kwargs):
        """
        a function to place tower when money is sufficient.
        NOTE: this function is deprecated, please use Tower.place(money=) to set money.

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
        return self

    def upgrade_with_order(self, order: list) :
        logger.debug(f"upgrade {self.name} with order {order}")
        sleep(0.1)
        move_to(self.x, self.y, wait=0.1)
        click(wait=0.1)
        for i in order:
            sleep(0.3)
            if i == 1:
                self._upgrade(1, 0, 0)
            if i == 2:
                self._upgrade(0, 1, 0)
            if i == 3:
                self._upgrade(0, 0, 1)
        click(wait=0.1)
        return self

    def sell(self) -> None:
        """
        sell the tower
        """
        logger.debug("sell %s", self.name)
        sleep(0.1)
        move_to(self.x, self.y, wait=0.1)
        click(wait=0.1)
        press(hotkey["sell"])

    def targeting(self, to: int):
        sleep(0.1)
        while to != 0:
            press(hotkey["target"], wait=0.05)
            to -= 1
        return self

    def change_targeting(self, to: int):
        logger.debug("change %s targeting by %d steps", self.name, to)
        sleep(0.1)
        move_to(self.x, self.y, wait=0.1)
        click(wait=0.1)
        while to != 0:
            press(hotkey["target"], wait=0.05)
            to -= 1
        click(wait=0.1)
        return self

    def _upgrade(self, path1: int, path2: int, path3: int):
        while path1 != 0:
            while self.check_for_upgrade(1):
                sleep(5)
            press(hotkey["path1"], wait=0.05)
            path1 -= 1
        while path2 != 0:
            while self.check_for_upgrade(2):
                sleep(5)
            press(hotkey["path2"], wait=0.05)
            path2 -= 1
        while path3 != 0:
            while self.check_for_upgrade(3):
                sleep(5)
            press(hotkey["path3"], wait=0.05)
            path3 -= 1

    @check()
    def check_for_upgrade(self, path: int) -> bool:
        """
            :return: False if the tower can be upgraded
        """
        y = 0
        x = 0
        if self.lr == "l":
            x = 337
        elif self.lr == "r":
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
        color = grab().load()[LEFT + x, TOP + y]
        if color[2] > 80:
            return True
        elif color[2] < 50:
            return False
        else:
            logger.warning("A problem in checking tower upgrade")
            return True


