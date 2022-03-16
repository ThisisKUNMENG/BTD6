import win32gui
import sys

classname = "UnityWndClass"
titlename = "BloonsTD6"


def get_window():
    # 获取句柄
    hwnd = win32gui.FindWindow(classname, titlename)
    if hwnd:
        # 获取窗口左上角和右下角坐标
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        print(left, top, right, bottom)
        print(right - left, bottom - top)
    else:
        print("please open BTD6")
        sys.exit(200)
    if right - left == 1616 and bottom - top == 939:
        pass
    else:
        print("please set the correct window size")
        sys.exit(201)
    return left, top, right, bottom


left, top, right, bottom = get_window()


left = left + 7

money = [left+288, top+46, left+380, top+84]