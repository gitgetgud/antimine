import keyboard
import time

while(True):
    if keyboard.is_pressed('q'):
        exit()





im1 = screenshot('Microsoft Minesweeper')
im1['im'].save("im1.png")
time.sleep(5)
im2 = screenshot('Microsoft Minesweeper',im1["coords"])
im2['im'].save("im2.png")
# if im:
    # im.show()
    # im.save("image.png")




# import time
# from helpers.screenshot import Screenshot
# from helpers.move import Move
# from random import randint
# from helpers.detect import Detect

# im=[]

# sc=Screenshot('Microsoft Minesweeper')

# init_im = sc.screenshot()
# init_im['im'].save("init_im.png")

# mv=Move(init_im["coords"][0:2],[220,220],[110,110],8,8)

# mv.to(randint(0,9),randint(0,9))
# mv.click()

# time.sleep(1)

# im.append(sc.screenshot())
# im[-1]['im'].save(f"im{len(im)}.png")

# time.sleep(1)

# dt=Detect("im1.png")

# dt.dt()
# for i in dt.get():
#     print(i)

