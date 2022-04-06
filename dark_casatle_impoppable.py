from BTD6_Automation import *

dark_castle = Game("dark castle", "impoppable")

dart1 = Tower("dart", 599, 586)
sub1 = Tower("sub", 903, 608)
dart2 = Tower("dart", 567, 624)
obyn = Tower("hero", 738, 404)
alch1 = Tower("alch", 842, 590)
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
farm1 = Tower("farm", 826, 90)
farm2 = Tower("farm", 690, 90)
farm3 = Tower("farm", 553, 95)
farm4 = Tower("farm", 803, 869)
farm5 = Tower("farm", 667, 869)


def dark_catsle_impoppable():
    dart1.place()
    obyn.place()
    Game.game_play()
    druid1.place_money(500)
    dart1.upgrade_to(path3=2)
    sub1.place_money(250)
    sub1.upgrade_with_order([1, 1, 3, 3])
    alch1.place_money(600, upgrade=[3, 2, 0])
    sub1.upgrade_to(path3=2)
    alch1.upgrade_to(path1=1)
    druid2.place_money(500)
    druid1.upgrade_to(path2=1, path3=4)
    druid3.place_money(500)
    druid2.upgrade_to(path2=1, path3=4)
    vil1.place_money(1500, upgrade=[2, 2, 0])
    alch2.place_money(700, upgrade=[4, 2, 0])
    druid4.place_money(500)
    druid5.place_money(500)
    druid6.place_money(500)
    farm1.place_money(1400)
    farm1.upgrade_with_order([3, 3, 3, 2, 2])
    druid3.upgrade_to(path2=1, path3=4)
    farm2.place_money(1500)
    farm2.upgrade_with_order([3, 3, 3, 2, 2])
    druid4.upgrade_to(path2=1, path3=4)
    druid5.upgrade_to(path2=1, path3=4)
    druid6.upgrade_to(path2=1, path3=4)
    alch3.place_money(700, upgrade=[3, 2, 0])
    druid2.upgrade_to(path3=1)
    vil1.upgrade_to(path2=1)
    spike1.place_money(1100, upgrade=[0, 2, 4])
    spike1.change_targeting(1)
    alch3.upgrade_to(path1=1)
    spike1.upgrade_to(path3=1)


if __name__ == "__main__":
    # 13659 XP / MIN
    # 22 MIN / GAME
    to_front()
    for i in range(1):
        try:
            print("current times:", i+1)
            dark_castle.ready()
            dark_catsle_impoppable()
            dark_castle.game_exit()
        except GameError as e:
            print("lost at ", i+1, " round with text ", e)
            dark_castle.lose_home()
