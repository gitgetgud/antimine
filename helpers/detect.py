import cv2
from helpers.color_values import *

class Detect:
    def __init__(self,filename,history=None,maxX=9,maxY=9):
        if history:
            self.res = history[-1]
        else:
            self.res = [[0 for x in range(maxX)] for y in range(maxY)]
        self.img=cv2.imread(filename)

    def _avgpos(self,pos,variance=30):
        res=[]
        for i in range(1,variance):
            res.append(pos+i)
        return res

    def _calc(self,val):
        return 200+(val*106)

    def _eq(self,color1,color2,variance=30):
        if abs(color1-color2)<variance:
            return True
        return False

    def _similarRgb(self,clr1,clr2):
        for i in range(0,3):
            if not self._eq(clr1[i],clr2[i]):
                return False
        return True

    def dt(self):
        for y in range(0,9):
            for x in range(0,9):
                if self.res[x][y] not in [0,"0","X"]:
                    continue
                tmpx=self._avgpos(self._calc(x))
                tmpy=self._avgpos(self._calc(y))
                for i in tmpx:
                    for j in tmpy:
                        for k,v in empts.items():
                            for t in v:
                                if self._similarRgb(self.img[i][j],t):
                                    self.res[x][y]=k
                                    break

        for y in range(0,9):
            for x in range(0,9):
                tmpx=self._avgpos(self._calc(x))
                tmpy=self._avgpos(self._calc(y))
                for i in tmpx:
                    for j in tmpy:
                        for k,v in vals.items():
                            for t in v:
                                if self._similarRgb(self.img[i][j],t):
                                    self.res[x][y]=k
                                    break

    def get(self):
        return self.res