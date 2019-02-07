import pyautogui
from random import randint

pyautogui.PAUSE = 1

pyautogui.FAILSAFE = True

def locate_buttons():
    try:
        accept = pyautogui.locateOnScreen('accept.png')
        acc_x = round(accept[0]+(accept[2]/2))
        acc_y = round(accept[1]+(accept[3]/2))
        acc_pos = [acc_x,acc_y]
    except:
        accept = None
    try:
        decline = pyautogui.locateOnScreen('decline.png')
        dec_x = round(decline[0]+(decline[2]/2))
        dec_y = round(decline[1]+(decline[3]/2))
        dec_pos = [dec_x,dec_y]
    except:
        decline = None
    print(acc_pos,dec_pos)
    return acc_pos,dec_pos

acc_pos,dec_pos = locate_buttons()

while True:
    random_int = randint(0,3)
    if random_int == 0:
        pyautogui.moveTo(acc_pos, duration=0.5)
        pyautogui.click()
    else:
        pyautogui.moveTo(dec_pos, duration=0.5)
        pyautogui.click()
