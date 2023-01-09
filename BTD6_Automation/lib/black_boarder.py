# This module is to get black boarder on a map.
# Note that this module is not completed yet.

from .utils import *
from .dicts import modes

special_modes = ["impoppable", "double hp moabs", "half cash", "ABR", "apopalypse",
                 "primary", "military", "magic", "reverse", "deflation"]


class BlackBoarder(object):
    def __init__(self, m, game_func, **kwargs):
        self.m = m
        self.game = {}
        for i in modes:
            self.game[i] = game_func

    def run(self):
        for i in modes:
            game = Game(self.m, i)
            game.ready()
            try:
                self.game[i]()
            except GameError:
                logger.warning("lost in game mode ", i)
                game.lose_home()
            else:
                logger.info("victory in game mode ", i)
                game.game_exit()
            finally:
                del game

    def special_run(self):
        pass

