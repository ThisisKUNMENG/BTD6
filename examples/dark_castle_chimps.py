from BTD6_Automation import *
import sys

dark_castle = Game("dark castle", "chimps")

dart1 = Tower("dart", 616, 579)
sub1 = Tower("sub", 905, 608)
dart2 = Tower("dart", 496, 541)
obyn = Tower("hero", 738, 404)
alch1 = Tower("alch", 845, 589)
druid1 = Tower("druid", 675, 403)
druid2 = Tower("druid", 611, 396)
druid3 = Tower("druid", 664, 349)
druid4 = Tower("druid", 728, 350)
druid5 = Tower("druid", 792, 347)
druid6 = Tower("druid", 801, 401)
vil1 = Tower("village", 713, 280)
alch2 = Tower("alch", 572, 357)
alch3 = Tower("alch", 615, 320)
spike1 = Tower("spike", 852, 318)
sub2 = Tower("sub", 917, 295)


def dark_castle_chimps():
    dart1.place()
    sub1.place()
    Game.game_play()
    dart2.place_money(225, targeting=1)
    obyn.place(money_t=700)
    sub1.upgrade_with_order([1, 1, 3, 3])
    dart1.upgrade_to(path3=2)
    sub1.upgrade_to(path3=2)
    alch1.place(upgrade=[3, 2, 0])
    alch1.upgrade_to(path1=1)
    druid1.place()
    druid2.place()
    druid3.place()
    druid4.place()
    druid5.place()
    druid6.place()
    vil1.place(upgrade=[2, 2, 0])
    druid1.upgrade_to(path2=1, path3=4)
    druid2.upgrade_to(path2=1, path3=4)
    druid3.upgrade_to(path2=1, path3=4)
    druid4.upgrade_to(path2=1, path3=4)
    druid5.upgrade_to(path2=1, path3=4)
    druid6.upgrade_to(path2=1, path3=4)
    alch2.place(upgrade=[4, 2, 0])
    alch3.place(upgrade=[3, 2, 0])
    druid2.upgrade_to(path3=1)
    vil1.upgrade_to(path2=1)
    spike1.place(upgrade=[0, 2, 4])
    spike1.change_targeting(1)
    alch3.upgrade_to(path1=1)
    spike1.upgrade_to(path3=1)
    sub2.place(upgrade=[0, 4, 0])




if __name__ == "__main__":
    to_front()
    while True:
        try:
            dark_castle_chimps()
        except GameError:
            print("lost")
            dark_castle.lose_restart()


