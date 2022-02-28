import time
from typing import Text
import pyautogui as pg

T = int(input("Delay \n"))
Text = input("Message \n")
Time  = int(input("Amount \n"))

time.sleep(15)

i = 0

while (i <= Time-1):
    time.sleep(T)
    pg.typewrite(Text)
    pg.press('enter')
    i += 1