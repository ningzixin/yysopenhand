import win32gui

# hwnd_title = dict()
#
#
# def get_all_hwnd(hwnd, mouse):
#     if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
#         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
#
#
# win32gui.EnumWindows(get_all_hwnd, 0)
#
# name  = 1
# for h, t in hwnd_title.items():
#     if t is not "":
#         print(h, t)
#         if t == '阴阳师-网易游戏':
#             name = h

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
def getGameImg():
    hwnd = win32gui.FindWindow(None, "阴阳师-网易游戏")
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img.save("screenshot.jpg")
    return img
