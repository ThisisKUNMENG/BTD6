"""
this module is to initialize BTD6 Automation module.
Specifically, it is to find the BTD6 window and define functions that imitate user input.
"""
from __future__ import annotations

import sys
from time import sleep

import win32gui
import logging
import pyautogui
import pydirectinput
import PIL.ImageGrab
import PIL.Image

CLASS_NAME = "UnityWndClass"
TITLE_NAME = "BloonsTD6"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger()


def get_window() -> tuple[int, int, int, int]:
    """
    find BTD6 window

    NOTE: BTD6 window size must be 1600*900
    """
    hwnd = win32gui.FindWindow(CLASS_NAME, TITLE_NAME)
    if hwnd:
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        logging.info("BTD6 on screen, proceeding")
        logging.info("BTD6 position: (%d, %d, %d, %d)", left, top, right, bottom)
    else:
        logging.error("please open BTD6")
        sys.exit(200)
    if right - left == 1616 and bottom - top == 939:
        pass
    else:
        logging.error("please set the correct window size")
        sys.exit(201)
    return left, top, right, bottom


LEFT, TOP, RIGHT, BOTTOM = get_window()

LEFT = LEFT + 7


def move_to(x: int, y: int, wait: float = 0.2) -> None:
    """
    move mouse to (x, y)
    """
    pyautogui.moveTo(LEFT + x, TOP + y)
    sleep(wait)


def click(wait: float = 0.5) -> None:
    """
    click mouse
    """
    pyautogui.click()
    sleep(wait)


def press(key: str, wait: float = 0.1) -> None:
    """
    press key
    """
    pydirectinput.press(key)
    sleep(wait)


def grab(*args):
    """
    grab screen, a wrapper of PIL.ImageGrab.grab
    """
    if not args:
        return PIL.ImageGrab.grab()
    elif isinstance(args[0], list):
        return PIL.ImageGrab.grab([LEFT + args[0][0], TOP + args[0][1], LEFT + args[0][2], TOP + args[0][3]])
    elif len(args) == 4:
        return PIL.ImageGrab.grab([LEFT + args[0], TOP + args[1], LEFT + args[2], TOP + args[3]])
    else:
        sys.exit(-1)
