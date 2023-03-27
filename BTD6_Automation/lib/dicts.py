# This module stores the stats of the game.

hotkey = {
    "dart": "q",
    "boom": "w",
    "bomb": "e",
    "tack": "r",
    "ice": "t",
    "glue": "y",
    "sniper": "z",
    "sub": "x",
    "boat": "c",
    "ace": "v",
    "heli": "b",
    "mortar": "n",
    "dartling": "m",
    "wizard": "a",
    "super": "s",
    "ninja": "d",
    "alch": "f",
    "druid": "g",
    "farm": "h",
    "engineer": "l",
    "spike": "j",
    "village": "k",
    "hero": "u",
    "path1": ",",
    "path2": ".",
    "path3": "/",
    "sell": "backspace",
    "target": "tab"
}

maps = {
    "monkey meadow":
        {
            "name": "monkey meadow",
            "level": "beginner",
            "page": 1,
            "pos": 1
        },
    "scrapyard":
        {
            "name": "scrapyard",
            "level": "beginner",
            "page": 1,
            "pos": 6
        },
    "middle of the road":
        {
            "name": "middle of the road",
            "level": "beginner",
            "page": 1,
            "pos": 4
        },
    "balance":
        {
            "name": "balance",
            "level": "intermediate",
            "page": 1,
            "pos": 3
        },
    "dark castle":
        {
            "name": "dark castle",
            "level": "expert",
            "page": 2,
            "pos": 3
        },
    "sanctuary":
        {
            "name": "sanctuary",
            "level": "expert",
            "page": 1,
            "pos": 2
        },
    "ravine":
        {
            "name": "ravine",
            "level": "expert",
            "page": 1,
            "pos": 3
        },
    "flooded valley":
        {
            "name": "flooded valley",
            "level": "expert",
            "page": 1,
            "pos": 4
        },
    "infernal":
        {
            "name": "infernal",
            "level": "expert",
            "page": 1,
            "pos": 5
        },
    "bloody puddles":
        {
            "name": "bloody puddles",
            "level": "expert",
            "page": 1,
            "pos": 6
        },
    "workshop":
        {
            "name": "workshop",
            "level": "expert",
            "page": 2,
            "pos": 1
        },
    "quad":
        {
            "name": "quad",
            "level": "expert",
            "page": 2,
            "pos": 2
        },
    "muddy puddles":
        {
            "name": "muddy puddles",
            "level": "expert",
            "page": 2,
            "pos": 4
        },
    "ouch":
        {
            "name": "ouch",
            "level": "expert",
            "page": 2,
            "pos": 5
        }

}

modes = {
    "easy standard":
        {
            "difficulty": "easy",
            "cord": [544, 517]
        },
    "primary":
        {
            "difficulty": "easy",
            "cord": [808, 409]
        },
    "deflation":
        {
            "difficulty": "easy",
            "cord": [1070, 409]
        },
    "medium standard":
        {
            "difficulty": "medium",
            "cord": [544, 517]
        },
    "military":
        {
            "difficulty": "medium",
            "cord": [808, 409]
        },
    "apopalypse":
        {
            "difficulty": "medium",
            "cord": [1070, 409]
        },
    "reverse":
        {
            "difficulty": "medium",
            "cord": [808, 650]
        },
    "hard standard":
        {
            "difficulty": "hard",
            "cord": [544, 517]
        },
    "magic":
        {
            "difficulty": "hard",
            "cord": [808, 409]
        },
    "double hp moabs":
        {
            "difficulty": "hard",
            "cord": [1070, 409]
        },
    "ABR":
        {
            "difficulty": "hard",
            "cord": [808, 650]
        },
    "impoppable":
        {
            "difficulty": "impoppable",
            "cord": [1070, 650]
        },
    "half cash":
        {
            "difficulty": "hard",
            "cord": [1350, 409]
        },
    "chimps":
        {
            "difficulty": "hard",
            "cord": [1350, 650]
        }
}

special_modes = ["impoppable", "double hp moabs", "half cash", "ABR", "apopalypse",
                 "primary", "military", "magic", "reverse", "deflation"]

tower_money_all = {
    "dart": {"easy": 170, "medium": 200, "hard": 215, "impoppable": 240},
    "boom": {"easy": 275, "medium": 325, "hard": 350, "impoppable": 390},
    "bomb": {"easy": 445, "medium": 525, "hard": 565, "impoppable": 630},
    "tack": {"easy": 240, "medium": 280, "hard": 300, "impoppable": 335},
    "ice": {"easy": 425, "medium": 500, "hard": 540, "impoppable": 600},
    "glue": {"easy": 235, "medium": 275, "hard": 295, "impoppable": 330},
    "sniper": {"easy": 300, "medium": 350, "hard": 380, "impoppable": 420},
    "sub": {"easy": 275, "medium": 325, "hard": 350, "impoppable": 390},
    "boat": {"easy": 425, "medium": 500, "hard": 540, "impoppable": 600},
    "ace": {"easy": 680, "medium": 800, "hard": 865, "impoppable": 960},
    "heli": {"easy": 1360, "medium": 1600, "hard": 1730, "impoppable": 1920},
    "mortar": {"easy": 640, "medium": 750, "hard": 810, "impoppable": 900},
    "dartling": {"easy": 720, "medium": 850, "hard": 920, "impoppable": 1020},
    "wizard": {"easy": 320, "medium": 375, "hard": 405, "impoppable": 450},
    "super": {"easy": 2125, "medium": 2500, "hard": 2700, "impoppable": 3000},
    "ninja": {"easy": 425, "medium": 500, "hard": 540, "impoppable": 600},
    "alch": {"easy": 470, "medium": 550, "hard": 595, "impoppable": 660},
    "druid": {"easy": 340, "medium": 400, "hard": 430, "impoppable": 480},
    "farm": {"easy": 1060, "medium": 1250, "hard": 1350, "impoppable": 1500},
    "engineer": {"easy": 340, "medium": 400, "hard": 430, "impoppable": 480},
    "spike": {"easy": 850, "medium": 1000, "hard": 1080, "impoppable": 1200},
    "village": {"easy": 1020, "medium": 1200, "hard": 1295, "impoppable": 1440}
}

pos_loc = [[429, 256], [813, 256], [1150, 256], [429, 515], [813, 515], [1150, 515]]
