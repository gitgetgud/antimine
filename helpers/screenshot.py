import pyautogui
import win32gui
import time


class Screenshot:
    def __init__(self,window_title=None,coords=None):
        self.window_title=window_title
        self.coords=coords


    def screenshot(self):
        if self.window_title:
            hwnd = win32gui.FindWindow(None, self.window_title)
            if hwnd:
                if self.coords == None:
                    win32gui.SetForegroundWindow(hwnd)
                    x, y, x1, y1 = win32gui.GetClientRect(hwnd)
                    x, y = win32gui.ClientToScreen(hwnd, (x, y))
                    x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
                    im = pyautogui.screenshot(region=(x, y, x1, y1))
                    return {
                        "im":im,
                        "coords":[
                            x,
                            y,
                            x1,
                            y1,
                        ]
                    }
                else:
                    im = pyautogui.screenshot(region=tuple(self.coords))
                    return {
                        "im":im,
                        "coords":self.coords
                    }
            else:
                print('Window not found!')
        else:
            time.sleep(3)
            im = pyautogui.screenshot()
            return {
                "im":im,
                "coords":self.coords
            }
