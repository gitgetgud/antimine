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