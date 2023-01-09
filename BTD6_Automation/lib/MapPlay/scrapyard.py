from ..utils import *
from ..tower import *


class Scrapyard:
    def __init__(self):
        pass

    def black_boarder(self):
        while True:
            for mode in ["hard standard", "ABR", "impoppable"]:
                g = Game("scrapyard", mode)
                g.ready()
                try:
                    game()
                except GameError as e:
                    pass
        pass


def game():
    hero = Tower("hero", 248, 278)
    wiz = Tower("wizard", 565, 384)
    heli = Tower("heli", 1087, 182)
    hero.place(money=850)
    wiz.place(upgrade=[0, 2, 2])
    heli.place(upgrade=[3, 2, 0])
    wiz.upgrade_with_order([3, 3, 3])
    heli.upgrade_with_order([1, 1])


if __name__ == "__main__":
    to_front()
    Scrapyard.black_boarder()
