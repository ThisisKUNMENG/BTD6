# BTD6 Automation


`BTD6_Automation` is a python package that provides functions to grind BTD6 XP or collection event and automate BTD6 game play.


---

## Guide for BTD6 Automation

* With `Game` class, you can control and automate the game page behavior in BTD6.
* With `Tower` class, you can develop your own strategy for a map and mode in BTD6 that has 99.99% reproducibility (there might have RNG).

### Requirements

* IMPORTANT: Set the BTD6 screen size at `1600 * 900`, otherwise the positioning will be wrong
* IMPORTANT: Set hotkey to default setting, otherwise the tower operation will be wrong since it depends on hotkey


### Functions

* `to_front`：let the BTD6 window be the front window by double clicking the center of BTD6 window.

* class `Game`: operate game page behavior

  * usage: `Game(map: str, difficulty: str)` 
    * Example: `game = Game("monkey meadow", "easy")`
  * class functions:
      * home operator
          * `ready`: enter the chosen map and mode from home page
            * Example: `game.ready()`
      * game operator
          * `game_play`: play and fast-forward the game
            * Example: `game.game_play()`
          * `game_exit`: exit to home page when the game is over (victory or lost)
            * Example: `game.game_exit()`
          * `free_play`: continue to free play
            * Example: `game.free_play()`

* class `Tower`: operate monkey tower behavior

  * usage: `Tower(tower name: str, x: int, y: int)`, `x` and `y` are the relative position of the tower on BTD6 window
    * Example: `tower = Tower("dart", 100, 100)`
  * `tower name` are recorded in `BTD6_Automation\lib\dicts.py`
  * class functions:
      * `place`: place the tower at the given position
        * arguments:
          * `upgrade`: upgrade the tower to the given level
            * Example: `tower.place(upgrade=[0,1,2])`
          * `targeting`: set the targeting of the tower (press `TAB` for a number of times)
            * Example: `tower.place(targeting=2)`
          * `money_t`: set the money of the tower (have default value which corresponds to mode played on)
            * Example: `tower.place(money_t=200)`
      * `upgrade_to`: upgrade the tower to the given level at certain path
        * Example: `tower.upgrade_to(path1=2, path2=3, path3=0)`
      * `upgrade_with_order`: upgrade the tower with given order.
        * note that the argument is a tuple or list that each element is 1-3 (the path number)
        * Example: `tower.upgrade_with_order([3,1,3])`
      * `sell`: sell the tower

* `json_to_play`: you can store game strategy into a json file, and you play the game with given json file.
  * The package provides example json files in `BTD6_Automation\lib\MapPlay\{map name}.json`
  * You can use `json_to_play("monkey meadow", "easy")` to implement the example strategy if I have written it.
  * Otherwise you can write your own strategy and use `json_to_play("monkey meadow", "easy", json_path=YOUR_JSON)` to implement strategy

* class `Collection`: grind collection event
  * IMPORTANT: please disable internet collection, otherwise the create open page will pop up and I have not written a function to close it.
  * usage `Collection("easy").grind`
