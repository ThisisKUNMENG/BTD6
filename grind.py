import sys

from findwindow import *
from time import sleep
from pyautogui import moveTo, click, scroll
from pydirectinput import press
import datetime

def open():
    click(left+400, top+400)
    sleep(0.3)
    click(left + 400, top + 400)
    sleep(0.3)
    click(left + 400, top + 400)
    sleep(0.3)
    moveTo(left+1000, top+460)
    sleep(0.3)
    click()
    sleep(1.5)
    for i in range(0, 20):
        scroll(-300)
        sleep(0.1)
    moveTo(left + 1000, top + 265)
    sleep(0.3)
    click()
    sleep(1)
    moveTo(left + 700, top + 690)
    sleep(0.3)
    click()
    sleep(0.3)
    sleep(5)


def place():
    click()
    sleep(0.3)
    # dartling
    press('m')
    sleep(0.3)
    moveTo(left + 1054, top + 595)
    sleep(0.3)
    click()
    sleep(0.3)
    click()
    sleep(0.3)
    for i in range(0, 5):
        press('.')
        sleep(0.1)
    press(',')
    sleep(0.1)
    press(',')
    sleep(0.1)
    # village
    press('k')
    sleep(0.3)
    moveTo(left + 1053, top + 494)
    click()
    sleep(0.3)
    click()
    sleep(0.3)
    press(',')
    sleep(0.1)
    press(',')
    sleep(0.1)
    # alch
    press('f')
    sleep(0.3)
    moveTo(left + 939, top + 554)
    click()
    sleep(0.3)
    click()
    sleep(0.3)
    press(',')
    sleep(0.1)
    press(',')
    sleep(0.1)
    press(',')
    sleep(0.1)
    press(',')
    sleep(0.1)
    press('.')
    sleep(0.1)
    press('.')
    sleep(0.1)
    # druid,
    press('g')
    sleep(0.3)
    moveTo(left + 302, top + 617)
    sleep(0.3)
    click()
    sleep(0.3)
    click()
    sleep(0.3)
    for i in range(0, 5):
        press('.')
        sleep(0.1)
    press(',')
    sleep(0.1)
    press(',')
    sleep(0.1)
    click()
    sleep(0.2)
    moveTo(left + 317, top + 680)
    sleep(0.2)


def grind():
    open()
    place()
    press('space')
    sleep(0.2)
    press('space')
    sleep(5)
    for i in range(0, 4):
        press('1')
        sleep(15)
    sleep(20)
    click()
    sleep(1)
    click()
    sleep(1)
    moveTo(left + 686, top + 726)
    sleep(0.3)
    click()
    sleep(1)
    moveTo(left + 500, top + 690)
    sleep(0.3)
    click()
    sleep(5)


if __name__ == "__main__":
    while True:
        grind()
        d = datetime.datetime.now()
        if d.hour == 15 and d.minute > 50:
            break

