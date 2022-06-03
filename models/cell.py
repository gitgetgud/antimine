class Cell:
    def __init__(self):
        self.value = 0
        self.mine_prob = None
        self.xscells = []

    def set(self,value):
        self.value = value

    def get(self):
        return self.value

    def is_numeric(self):
        if self.value in map(str,range(1,9)):
            return True
        return False

    def __str__(self) -> str:
        return str(self.value)

    def is_mine(self,value=1.0):
        self.mine_prob = value

    def check_surr4mines(self):
        if self.value.isnumeric():
            if int(self.value) == len(self.xscells):
                for i in self.xscells:
                    i.is_mine(1)
    
    def check_surr4safe(self):
        if self.value.isnumeric():
            psum=0
            if int(self.value) < len(self.xscells):
                for i in self.xscells:
                    if i.mine_prob == 1.0:
                        psum+=1
            if psum == int(self.value):
                for i in self.xscells:
                    if i.mine_prob == None:
                        i.mine_prob=0.0


