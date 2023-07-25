from machine import SoftI2C,Pin,UART,Timer,SPI
import time
from utils.drivers import KEYBOARD
from utils.drivers import SCREEN
from utils.fbconsole import FBConsole
import utils.color as color
import os
import st7789

screen=SCREEN(320,240)
kb=KEYBOARD()
screen.tft.jpg('logo.jpg',0,0)
time.sleep(1)
theme=color.COLOR_EVA
scr = FBConsole(screen,bg_color=theme['bg2'],fg_color=theme['font'])
os.dupterm(scr)   
print('MPY CONSOLE 1.00 by jd3096')
time.sleep(0.5)

def check_key(t):
    re=kb.check_key()
    if re!=None:
        if len(re)==1:
            scr._c=re
            scr._press()
        else:
            for b in re:
                scr._c=b.to_bytes(1,'big')
                scr._press()
    
tim=Timer(0)
tim.init(mode=Timer.PERIODIC, period=10, callback=check_key)





