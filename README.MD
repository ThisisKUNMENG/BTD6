# BTD6 Automation


`BTD6_Automation` is a python package that provides functions to grind BTD6 XP or collection event, test BTD6 game play.

* TODO:
    * automate the Black boarder of a map
    * refine coding
    * complete documentation

---

# A guide for BTD6 Automation

## Requirements

* Set the BTD6 screen size at `1600 * 900`, otherwise the positioning will be wrong

## Functions

### Basic functions

#### `to_front`

#### class `Game` 

* usage: `Game(map: str, difficulty: str)` 
* class functions:
    * home operator
        * `ready`
    * game operator
        * `game_play`
        * `game_exit`
        * `free_play`

#### class `Tower`

* usage: `Tower(tower name: str, position_x: int, position_y: int)` 
* class functions:
    * `place`

### class `Collection`

* usage `Collection("easy").grind`

### class `BlackBoarder`

* not finished