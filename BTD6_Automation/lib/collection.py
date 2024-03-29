# This is a module to grind collection event

from .utils import *
from .tower import *
from .json_parse import json_to_play


class Collection:
    """
    grind collection event (expert map easy mode)
    use `Collection("easy").grind()` to start
    """
    def __init__(self, difficulty: str):
        self.difficulty = difficulty
        self.map = ""

    def _grind_once(self) -> None:
        while check_need_collect():
            move_to(807, 606)
            click(wait=2)
            collect()

        move_to(765, 56)
        click()
        Game.play()
        _to_expert()
        pos_x, pos_y, page = _find_bonus_and_enter()
        self.map = _find_map(pos_x, pos_y, page)
        logger.info("collection bonus map is " + self.map)
        if self.difficulty == "easy":
            g = Game(self.map, "easy standard")
            move_to(530, 390, wait=2)
            click(wait=1)
            move_to(modes["easy standard"]["cord"][0], modes["easy standard"]["cord"][1], wait=2)
            click(wait=9)
            click(wait=5)
            self._easy_play()
            g.game_exit()

    def _easy_play(self) -> None:
        if self.map == "infernal" or self.map == "ouch" or self.map == "bloody puddles" or self.map == "muddy puddles":
            Tower("hero", 1336, 450).place_money(765, targeting=3)
            Game.game_play()
            Tower("sniper", 1340, 583).place(upgrade=[2, 0, 4])
        elif self.map == "dark castle":
            Tower("hero", 1336, 480).place_money(765, targeting=3)
            Game.game_play()
            Tower("sniper", 1217, 480).place(upgrade=[2, 0, 4])
        elif self.map == "quad":
            Tower("hero", 450, 476).place_money(765, targeting=3)
            Game.game_play()
            Tower("sniper", 923, 476).place(upgrade=[2, 0, 4])
        elif self.map == "sanctuary":
            Tower("hero", 746, 232).place_money(765, targeting=3)
            Game.game_play()
            Tower("sniper", 1200, 375).place(upgrade=[2, 0, 4])
        elif self.map == "flooded valley":
            Tower("hero", 167, 673).place_money(765, targeting=3)
            Game.game_play()
            Tower("sniper", 233, 691).place(upgrade=[2, 0, 4])
        elif self.map == "ravine":
            Tower("hero", 182, 834).place_money(765, targeting=3)
            Game.game_play()
            _ace = Tower("ace", 1066, 407)
            _ace.place(upgrade=[0, 0, 3])
            _ace.upgrade_to(path2=2)
            Tower("alch", 1088, 303).place(upgrade=[4, 2, 0])
        elif self.map == "workshop":
            Tower("hero", 513, 411).place_money(765, targeting=3)
            Game.game_play()
            Tower("sniper", 843, 449).place(upgrade=[2, 0, 4])
        elif self.map == "dark dungeons":
            Tower("hero", 307, 682).place_money(765, targeting=3)
            Game.game_play()
            _ace = Tower("ace", 890, 526)
            _ace.place(upgrade=[0, 0, 3])
            _ace.upgrade_to(path2=2)
            Tower("alch", 857, 424).place(upgrade=[4, 2, 0])
        elif self.map == "glacial trail":
            json_to_play(self.map, "easy standard")
        else:
            raise GameError("map play to be defined")

    def grind(self, times: int = -1) -> None:
        _times = 0
        if times == -1:
            while True:
                _times += 1
                logger.info(f"grind times: {_times}")
                self._grind_once()
        else:
            for i in range(times):
                _times += 1
                logger.info(f"grind times: {_times}, remaining times: {times - _times}")
                self._grind_once()


def _to_expert() -> None:
    move_to(1111, 850)
    click(wait=2)


_x_pos = [593, 946, 1300]
_y_pos = [271, 542]


def _find_bonus_and_enter() -> tuple[int, int, int]:
    p = grab().load()
    # note expert map
    for x in _x_pos:
        for y in _y_pos:
            if _check_is_bonus(p, x, y):
                pass
            else:
                move_to(x, y)
                click(wait=2)
                return _x_pos.index(x), _y_pos.index(y), 1
    click()
    sleep(2)
    p = grab().load()
    for y in _y_pos:
        for x in _x_pos:
            if _check_is_bonus(p, x, y):
                pass
            else:
                move_to(x, y)
                click(wait=2)
                return _x_pos.index(x), _y_pos.index(y), 2
    raise GameError("can not find a map with bonus")


def _find_map(x, y, page) -> str:
    for inf in maps.values():
        if inf["level"] == "expert" and inf["page"] == page and inf["pos"] == ((x + 1) + 3 * y):
            return inf["name"]
    raise GameError("map not found")


def _check_is_bonus(p, x, y) -> bool:
    return (
            p[LEFT + x, TOP + y][0] in range(197, 201) and
            p[LEFT + x, TOP + y][1] in range(161, 165) and
            p[LEFT + x, TOP + y][2] in range(108, 112)  # normal yellow
    ) or (
            p[LEFT + x, TOP + y][0] in range(180, 189) and
            p[LEFT + x, TOP + y][1] in range(200, 215) and
            p[LEFT + x, TOP + y][2] in range(105, 125)  # normal silver
    ) or (
            p[LEFT + x, TOP + y][0] in range(210, 230) and
            p[LEFT + x, TOP + y][1] in range(130, 150) and
            p[LEFT + x, TOP + y][2] in range(10, 25)    # normal bronze
    ) or (
            p[LEFT + x, TOP + y][0] in range(20, 30) and
            p[LEFT + x, TOP + y][1] in range(30, 40) and
            p[LEFT + x, TOP + y][2] in range(45, 55)    # black border
    )


