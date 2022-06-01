import enum
from tabnanny import check
import pyautogui as pg

class Move:
    def __init__(self,initCoord,firstCell,cellSpacing,maxX,maxY):
        pg.moveTo(*initCoord)
        pg.move(*firstCell)
        self.cellSpacingX=cellSpacing[0]
        self.cellSpacingY=cellSpacing[1]
        self.maxX=maxX
        self.maxY=maxY
        self.curX=0
        self.curY=0

    def check(self,x,y):
        if x<0 or y<0:
            raise Exception(f"Out of bounds(negative): x:{x},y:{y}")
        elif x>self.maxX or y>self.maxY:
            raise Exception(f"Out of bounds(over): x:{x},y:{y}")

    def to(self,x,y):
        self.check(x,y)
        rx=x-self.curX
        ry=y-self.curY
        pg.move(rx*self.cellSpacingX,ry*self.cellSpacingY)
        self.curX=x
        self.curY=y

    def click(self):
        pg.click()