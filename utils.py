from findwindow import *
from time import sleep
from pyautogui import moveTo, click
import pyautogui
from pydirectinput import press
from PIL.ImageGrab import grab


def to_front():
    moveTo(left+400, top+400)
    sleep(0.1)
    click()
    sleep(0.1)
    click()
    sleep(0.5)


class Game:
    def __init__(self, t):
        self.t = t

    @staticmethod
    def game_play():
        sleep(0.1)
        press("space")
        sleep(0.1)
        press("space")
        sleep(0.1)

    @staticmethod
    def game_exit():
        sleep(2)
        click()
        sleep(0.5)
        moveTo(left+800, top+800)
        sleep(0.5)
        click()
        sleep(3)
        moveTo(left+580, top+733)
        sleep(0.5)
        click()
        sleep(2)
        click()
        sleep(2)

    @staticmethod
    def play():
        sleep(5)
        moveTo(left+700, top+850)
        sleep(0.5)
        click()
        sleep(4)
        moveTo(left+1111, top+850)
        sleep(0.2)
        click()
        sleep(2)
        click()
        sleep(2)
        moveTo(left+813, top+238)
        sleep(2)
        click()
        sleep(1)
        moveTo(left+530, top+390)
        sleep(2)
        click()
        sleep(1)
        moveTo(left+1077, top+416)
        sleep(2)
        click()
        sleep(9)
        click()
        sleep(5)

    def ready(self):
        pass

    def check_upgrade(self):
        sleep(0.1)
        moveTo(left+510, top+672)
        tt = self.t
        while tt > 0:
            print("supposed game time remaining: " + str(tt) + " seconds")
            sleep(10)
            click()
            sleep(0.1)
            click()
            press("space")
            sleep(0.05)
            press("space")
            sleep(0.05)
            tt -= 10


