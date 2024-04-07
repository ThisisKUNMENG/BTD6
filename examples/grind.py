from BTD6_Automation import json_to_play, to_front, Game

dark_castle = Game("dark castle", "impoppable")
to_front()
loop = 1
while loop < 100:
    print("repeated times: " + str(loop))
    dark_castle.ready()
    json_to_play("dark castle", "impoppable")
    dark_castle.game_exit()
    loop += 1
