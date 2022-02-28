import time
import pyautogui as pg
import pyfiglet

name = pyfiglet.figlet_format("WaBomb")
print(name)

created_by = "\033[1;34m [#] Created By : Tushar Bhanushali \n"
print(created_by)

war = "\033[1;31m * Warning : This Tool was Just Made For Fun Don't Misuse it if anyone misuses it, it's not creator's reponsiblity * \n"
print(war)

ver = "\033[1;34m [#] Version : 1.0.0 \n"
print(ver)

T = int(input("[+] Enter Delay in seconds : "))
Text = input("[+] Enter Message : ")
Time  = int(input("[+] Enter Amount : "))

time.sleep(15)

i = 0

while (i <= Time-1):
    time.sleep(T)
    pg.typewrite(Text)
    pg.press('enter')
    i += 1

time.sleep(5)

made_by = "\n \033[1;32m [ \u2713 ] Created By : Tushar Bhanushali \n"
print(made_by)

vers = "\n \033[1;32m [ \u2713 ] Version : 1.0.0 \n"
print(vers)

success_msg = "\n \033[1;32m [ \u2713 ] Messages Were Sent ! \n"
print(success_msg)
