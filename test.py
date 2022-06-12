from models.board import Board
from models.window import Window
import constants.constants as consts
from helpers.detect import Detect
from helpers.move import Move
import time

w=Window()
w.resize(*consts.WINDOW_SIZE)
w.screenshot()
m=Move(w)
time.sleep(1)
dt=Detect(filename="im.png")
dt.dt()
for i in dt.get():
    print(i)
b=Board(init=dt.get())
b.mark_xscells()
b.mines_and_safe()
print(b.safe)
for i in b.safe:
    m.click(i[1],i[0],True)
    time.sleep(1)