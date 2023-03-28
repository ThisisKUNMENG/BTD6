# this module is to locate BTD6 window

import win32gui
import sys
import logging

classname = "UnityWndClass"
titlename = "BloonsTD6"
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger()


def get_window():
    """
    find BTD6 window

    NOTE: BTD6 window size must be 1600*900
    """
    hwnd = win32gui.FindWindow(classname, titlename)
    if hwnd:
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        logging.info("BTD6 on screen, proceeding", left, top, right, bottom)
    else:
        logging.error("please open BTD6")
        sys.exit(200)
    if right - left == 1616 and bottom - top == 939:
        pass
    else:
        logging.error("please set the correct window size")
        sys.exit(201)
    return left, top, right, bottom


left, top, right, bottom = get_window()


left = left + 7

money = [left+305, top+48, left+400, top+83]

if __name__ == "__main__":
    print(left, top, right, bottom)
