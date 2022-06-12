

class Cell:
    def __init__(self) -> None:
        self.value=0
        self.mine_prob=None
        self.xscells=[]

    def __str__(self) -> str:
        return str(self.value)

    def check_surr_4mines(self):
        if str(self.value).isnumeric():
            if int(self.value) == len(self.xscells):
                for i in self.xscells:
                    i.mine_prob=1.0

    def check_surr_4safe(self):
        if str(self.value).isnumeric():
            mnum=0
            if int(self.value) < len(self.xscells):
                for i in self.xscells:
                    if i.mine_prob != 1.0:
                        i.mine_prob = 0.0


    def check_surr(self):
        if str(self.value).isnumeric():
            msum=0 # number of surrounding mines
            if int(self.value) == len(self.xscells):# If current cell value is equal to the number of X cells, all of the X cells are mines
                for i in self.xscells:
                    i.mine_prob=1.0
            elif int(self.value) < len(self.xscells):
                for i in self.xscells:
                    if i.mine_prob == 1.0:
                        msum+=1
            if msum == int(self.value):
                for i in self.xscells:
                    if i.mine_prob == None:
                        i.mine_prob=0.0