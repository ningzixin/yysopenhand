
'''

'''
# from utils import gameinit
import pymouse, pykeyboard, os, sys
from pymouse import *
from pykeyboard import PyKeyboard
import time
from PyQt5.QtGui import *
import sys
import win32gui,win32api
import win32con
def iniGame():
    #设置窗体位置
    hwnd = win32gui.FindWindow(None, "阴阳师-网易游戏")
    if int(hwnd) <= 0:
        print("游戏未启动")
        return
    win32gui.SetForegroundWindow(hwnd)
import time
import win32api,win32gui,win32con
from ctypes import *
def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)
def moveCurPos(x,y):
    windll.user32.SetCursorPos(x, y)
def getCurPos():
    return win32gui.GetCursorPos()

def process():
    # iniGame()
    #点击
    x = 514
    y = 444
    m = PyMouse()
    while True:

        m.click(x, y, 1, 1)
        time.sleep(3)
# process()

