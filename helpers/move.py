import pyautogui as pg
from models.window import Window
import constants.constants as consts

X_INIT_MARGIN=consts.X_INIT_MARGIN
Y_INIT_MARGIN=consts.Y_INIT_MARGIN


class Move:
    def __init__(self,wobj:Window,cellSpacing,maxX=9,maxY=9):
        self.wobj=wobj
        self.refreshWindowLocation()
        self.cellSpacingX=cellSpacing[0]
        self.cellSpacingY=cellSpacing[1]
        self.maxX=maxX
        self.maxY=maxY

    def refreshWindowLocation(self):
        tmp=self.wobj.getLocation()
        self.initX=tmp['wstart'][0]+X_INIT_MARGIN
        self.initY=tmp['wstart'][1]+Y_INIT_MARGIN

    def check(self,x,y):
        if x<0 or y<0:
            raise Exception(f"Out of bounds(negative): x:{x},y:{y}")
        elif x>self.maxX or y>self.maxY:
            raise Exception(f"Out of bounds(over): x:{x},y:{y}")

    def click(self,x,y):
        self.check(x,y)
        tx=self.initX+(x*self.cellSpacingX)
        ty=self.initY+(y*self.cellSpacingY)
        pg.moveTo(tx,ty)