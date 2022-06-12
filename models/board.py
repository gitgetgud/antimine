from models.cell import Cell

class Board:
    def __init__(self,maxX,maxY,init=None) -> None:
        self.maxX=maxX
        self.maxY=maxY
        self.cells=[[Cell() for x in range(maxX)] for y in range(maxY)]
        if init:
            pass