import win32gui
from constants.constants import WINDOW_TITLE,SCREENSHOT_NAME
import pyautogui as pg

class Window:
    def __init__(self,window_title:str=WINDOW_TITLE) -> None:
        try:
            self.wind = win32gui.FindWindow(None, window_title)
        except Exception as e:
            print("Window not found: {}".format(str(e)))
        self.focus()


    def focus(self):
        win32gui.SetForegroundWindow(self.wind)

    def getLocation(self):
        x, y, x1, y1 = win32gui.GetClientRect(self.wind)
        x, y = win32gui.ClientToScreen(self.wind, (x, y))
        return {
            "wstart":[x,y],
            "screenshot":[x,y,x1,y1],
            "wend":[x+x1,y+y1]
        }

    def screenshot(self,filename=SCREENSHOT_NAME):
        pg.screenshot(region=tuple(self.getLocation()['screenshot'])).save(filename)

    def resize(self,width,height):
        x0, y0, x1, y1 = win32gui.GetWindowRect(self.wind)
        w = x1 - x0
        h = y1 - y0
        win32gui.MoveWindow(self.wind, x0, y0, width, height, True)


def screenshot(x,y,x1,y1,filename=SCREENSHOT_NAME)->None:
    # Take screenshot of the area. xy->starting point. X1Y1 stretch to ending point(relative,not absolute)
    pg.screenshot(region=(x,y,x1,y1)).save(filename)