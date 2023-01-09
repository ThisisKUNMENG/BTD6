from pydirectinput import moveTo, click
from time import sleep
from PIL.ImageGrab import grab


def varify_race():
    if grab().load()[1542, 310] == (52, 48, 47):
        return False
    else:
        return True


def race_entry():
    while varify_race():
        sleep(1)
    moveTo(1528, 339)
    sleep(0.2)
    click()
    sleep(2)
    moveTo(718, 745)
    sleep(0.2)
    click()
    sleep(10)
    sleep(0.2)
    click()
    sleep(2)
    click()
    sleep(1)
    moveTo(1333, 58)
    sleep(0.2)
    click()
    sleep(1)
    moveTo(803, 736)
    sleep(0.2)
    click()
    sleep(3)


if __name__ == "__main__":
    print(grab().load()[1542, 310])
    sleep(1)
    for i in range(50):
        race_entry()
