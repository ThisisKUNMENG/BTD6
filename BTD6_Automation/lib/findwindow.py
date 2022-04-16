# this module is to locate BTD6 window

import win32gui
import sys
import logging

classname = "UnityWndClass"
titlename = "BloonsTD6"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger()


def get_window():
    # 获取句柄
    hwnd = win32gui.FindWindow(classname, titlename)
    if hwnd:
        # 获取窗口左上角和右下角坐标
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        logging.info("BTD6 on screen, position at: %d, %d, %d, %d", left, top, right, bottom)
        # print(right - left, bottom - top)
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

money = [left+288, top+46, left+380, top+84]

if __name__ == "__main__":
    print(left, top, right, bottom)
