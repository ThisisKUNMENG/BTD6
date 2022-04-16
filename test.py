import easyocr
import json
from BTD6_Automation import *
from PIL.ImageGrab import grab
import numpy as np
import win32gui
# import pytesseract
from pydirectinput import moveTo, click
from time import sleep

# reader = easyocr.Reader(['en'], gpu = False)

if __name__ == '__main__':
    # print(grab().load()[946, 271])
    to_front()
    c = Collection("easy")
    c.grind()
