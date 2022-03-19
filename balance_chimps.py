from BTD6_Automation import *

sauda = Tower("hero", 702, 344)
tack1 = Tower("tack", 701, 492)
alch1 = Tower("alch", 818, 362)
vil1 = Tower("village", 821, 488)
druid1 = Tower("druid", 850, 620)
alch2 = Tower("alch", 590, 500)
sniper1 = Tower("sniper", 895, 775)


def balance_chimps():
    sauda.place()
    Game.game_play()
    sleep(5)
    tack1.place_money(310)
    tack1.upgrade_with_order([1, 1, 3, 3, 1, 1])
    alch1.place_money(600, upgrade=[4, 0, 1])
    vil1.place_money(1300, upgrade=[2, 2, 0])
    tack1.upgrade_to(path1=1)
    druid1.place_money(450, upgrade=[2, 5, 0])
    vil1.upgrade_to(path2=1)
    alch2.place_money(600, upgrade=[4, 2, 0])
    sniper1.place_money(400, upgrade=[4, 2, 0], targeting=3)


if __name__ == "__main__":
    # 11557.5 XP / MIN
    # 22 MIN / GAME
    to_front()
    balance_chimps()







