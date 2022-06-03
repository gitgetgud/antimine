import time
from helpers.screenshot import Screenshot
from helpers.move import Move
from random import randint
from helpers.detect import Detect
from models.board import Board
import keyboard

im=[]

sc=Screenshot('Microsoft Minesweeper')

init_im = sc.screenshot()
init_im['im'].save("init_im.png")

mv=Move(init_im["coords"][0:2],[220,220],[110,110],8,8)

mv.to(randint(0,9),randint(0,9))
mv.click()

time.sleep(5)
tomove=[]
while(True):
    if keyboard.is_pressed('q'):
        exit()

    if keyboard.is_pressed('r'):
        im.append(sc.screenshot())
        im[-1]['im'].save(f"im{len(im)}.png")
        dt=Detect(f"im{len(im)}.png")
        dt.dt()
        print("Detection done")


    if keyboard.is_pressed('p'):
        for i in dt.get():
            print(i)
    
    if keyboard.is_pressed('a'):
        b=Board(9,9,dt.get())
        b.analyze_mines()
        b.analyze_safe()
        tomove=b.get_safe()

    if keyboard.is_pressed('c'):
        print(tomove)
        for i in tomove:
            mv.to(i[0],i[1])
            mv.click()


