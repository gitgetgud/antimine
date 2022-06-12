from models.window import Window
import constants.constants as consts
from helpers.detect import Detect

# w=Window()
# print(w.getLocation())
# w.resize(*consts.WINDOW_SIZE)
# w.screenshot()

dt=Detect(filename="im.png")
dt.dt()
for i in dt.get():
    print(i)