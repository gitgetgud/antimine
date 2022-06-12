from models.cell import Cell
import constants.constants as consts

MAX_X=consts.MAX_X
MAX_Y=consts.MAX_Y

class Board:
    def __init__(self,maxX=MAX_X,maxY=MAX_Y,init=None) -> None:
        self.maxX=maxX
        self.maxY=maxY
        self.cells=[[Cell() for x in range(maxX)] for y in range(maxY)]
        self.safe=[]
        if init:
            self._read_ar(init)

    def __getitem__(self, key):
        return self.cells[key]

    def _loop(self,f):
        for y in range(0,self.maxY):
            for x in range(0,self.maxX):
                f(x,y)

    def _check(self,value,max):
        if value < 0 or value >= max:
            return False
        return True

    def mark_xscells(self):
        def f(x,y):
            if str(self.cells[x][y].value).isnumeric():
                for spx in range(-1,2):
                    for spy in range(-1,2):
                        if spx == 0 and spy==0:
                            continue
                        if self.check_out_of_bounds(x+spx,y+spy):
                            if self.cells[x+spx][y+spy].value == "X":
                                self.cells[x][y].xscells.append(self.cells[x+spx][y+spy])
        self._loop(f)

    def mines_and_safe(self):
        def mines(x,y):
            self.cells[x][y].check_surr_4mines()

        def safe(x,y):
            self.cells[x][y].check_surr_4safe()

        self._loop(mines)
        self._loop(safe)
        self._get_safe()


    def check_out_of_bounds(self,x,y):
        if self._check(x,self.maxX) and self._check(y,self.maxY):
            return True
        return False


    def _read_ar(self,ar):
        def f(x,y):
            self.cells[x][y].value=ar[x][y]
        self._loop(f)

    def debug(self,f=str):
        for i in self.cells:
            tmp=[]
            for j in i:
                tmp.append(f(j))
            print(tmp)

    def _get_safe(self):
        def f(x,y):
            if self.cells[x][y].mine_prob == 0.0:
                self.safe.append([x,y])
        self._loop(f)
