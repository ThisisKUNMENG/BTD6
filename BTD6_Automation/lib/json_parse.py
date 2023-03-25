from .findwindow import *
from .dicts import *
from .tower import Tower
from .utils import *
import json
import os


def json_to_play(m, mode):
    this_dir, _ = os.path.split(__file__)
    with open(this_dir + "/MapPlay/" + m + ".json", "r") as f:
        map_play = json.load(f)
    _mode_play(map_play, m, mode)


def _mode_play(map_play, m, mode):
    game = Game(m, mode)
    mode_play_j = map_play[mode]
    # create dicts for each tower and call them to place/upgrade
    tower_dict = {}
    for i in mode_play_j["Tower"]:
        temp = mode_play_j["Tower"][i]
        tower_dict[i] = Tower(temp["name"], temp["pos"][0], temp["pos"][1])
    for j in mode_play_j["sequence"]:
        if j == "Play":
            game.game_play()
        elif j["func"] == "place":
            ar = _parse_arg(j["arg"], "place")
            tower_dict[j["name"]].place(upgrade=ar[0], targeting=ar[1], money_t=ar[2])
        elif j["func"] == "upgrade_to":
            ar = _parse_arg(j["arg"], "upgrade_to")
            tower_dict[j["name"]].upgrade_to(path1=ar[0], path2=ar[1], path3=ar[2])
        elif j["func"] == "targeting":
            ar = _parse_arg(j["arg"], "targeting")
            tower_dict[j["name"]].targeting(to=ar)


def _parse_arg(a, func):
    ar = []
    if func == "place":
        ar = [None, 0, 0]
        for i in a:
            if i == "upgrade":
                ar[0] = a[i]
            if i == "targeting":
                ar[1] = a[i]
            if i == "money":
                ar[2] = a[i]
    if func == "upgrade_to":
        ar = [0, 0, 0]
        for i in a:
            if i == "path1":
                ar[0] = a[i]
            if i == "path2":
                ar[1] = a[i]
            if i == "path3":
                ar[2] = a[i]
    if func == "targeting":
        ar = a["to"]

    return ar


