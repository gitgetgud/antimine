from tabnanny import check
from models.cell import Cell

class Board:
    def __init__(self,maxX,maxY,init=None):
        self.maxX=maxX
        self.maxY=maxY
        self.cells=[[Cell() for x in range(maxX)] for y in range(maxY)]
        if init:
            self._read_ar(init)

    def __getitem__(self, key):
        return self.cells[key]

    def _loop(self,f):
        for y in range(0,self.maxY):
            for x in range(0,self.maxX):
                f(x,y)

    def _read_ar(self,ar):
        def f(x,y):
            self.cells[x][y].set(ar[x][y])
        self._loop(f)


    def analyze_mines(self):
        def f(x,y):
            if self.cells[x][y].is_numeric():
                for spx in range(-1,2):
                    for spy in range(-1,2):
                        if spx == 0 and spy ==0:
                            continue
                        if self.check(x+spx,self.maxX) and self.check(y+spy,self.maxY):
                            if self.cells[x+spx][y+spy].get() == "X":
                                self.cells[x][y].xscells.append(self.cells[x+spx][y+spy])
                self.cells[x][y].check_surr4mines()

        self._loop(f)

    def analyze_safe(self):
        def f(x,y):
            self.cells[x][y].check_surr4safe()
        self._loop(f)

    def get_safe(self):
        res=[]
        def f(x,y):
            if self.cells[x][y].mine_prob == 0.0:
                res.append((y,x))
        self._loop(f)
        return res

    def check(self,value,max):
        if value < 0 or value >= max:
            return False
        return True

    def debug(self,f=str):
        for i in self.cells:
            tmp=[]
            for j in i:
                tmp.append(f(j))
            print(tmp)