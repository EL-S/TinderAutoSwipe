import pyautogui
from random import randint
from time import sleep

# Any duration less than this is rounded to 0.0 to instantly move the mouse.
pyautogui.MINIMUM_DURATION = 0  # Default: 0.1
# Minimal number of seconds to sleep between mouse moves.
#pyautogui.MINIMUM_SLEEP = 0  # Default: 0.05
# The number of seconds to pause after EVERY public function call.
pyautogui.PAUSE = 0  # Default: 0.1

pyautogui.FAILSAFE = True

def locate_buttons():
    try:
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
    except UnboundLocalError:
        print("You need Tinder on the primary screen.")
        acc_pos,dec_pos = locate_buttons()
    return acc_pos,dec_pos


acc_pos,dec_pos = locate_buttons()

def smoother_move(new_pos):
    while True:
        flag_1 = False
        flag_2 = False
        
        current_pos = pyautogui.position()
        temp_x = current_pos[0]
        temp_y = current_pos[1]

        min_step_size = 25
        max_step_size = 35
        
        if (temp_x-new_pos[0]) <= -25 :
            temp_x += randint(min_step_size,max_step_size)
            flag_1 = False
        elif (temp_x-new_pos[0]) >= 25:
            temp_x -= randint(min_step_size,max_step_size)
            flag_1 = False
        else:
            random_num = randint(0,1)
            if random_num == 0:
                temp_x += randint(min_step_size,max_step_size)
            else:
                temp_x -= randint(min_step_size,max_step_size)
            flag_1 = True
        if (temp_y-new_pos[1]) >= 25:
            temp_y -= randint(min_step_size,max_step_size)
            flag_2 = False
        elif (temp_y-new_pos[1]) <= -25:
            temp_y += randint(min_step_size,max_step_size)
            flag_2 = False
        else:
            random_num = randint(0,1)
            if random_num == 0:
                temp_y += randint(min_step_size,max_step_size)
            else:
                temp_y -= randint(min_step_size,max_step_size)
            flag_2 = True
        if flag_1 == True and flag_2 == True:
            return
        else:
            smooth_move(new_pos)

def smooth_move(new_pos):
    while True:
        flag_1 = False
        flag_2 = False
        
        current_pos = pyautogui.position()
        temp_x = current_pos[0]
        temp_y = current_pos[1]

        min_step_size = 0
        max_step_size = 2
        
        if (temp_x-new_pos[0]) <= -15 :
            temp_x += randint(min_step_size,max_step_size)
            flag_1 = False
        elif (temp_x-new_pos[0]) >= 15:
            temp_x -= randint(min_step_size,max_step_size)
            flag_1 = False
        else:
            random_num = randint(0,1)
            if random_num == 0:
                temp_x += randint(min_step_size,max_step_size)
            else:
                temp_x -= randint(min_step_size,max_step_size)
            flag_1 = True
        if (temp_y-new_pos[1]) >= 15:
            temp_y -= randint(min_step_size,max_step_size)
            flag_2 = False
        elif (temp_y-new_pos[1]) <= -15:
            temp_y += randint(min_step_size,max_step_size)
            flag_2 = False
        else:
            random_num = randint(0,1)
            if random_num == 0:
                temp_y += randint(min_step_size,max_step_size)
            else:
                temp_y -= randint(min_step_size,max_step_size)
            flag_2 = True
        if flag_1 == True and flag_2 == True:
            return
        else:
            sleep(0.002)
            pyautogui.moveTo(temp_x, temp_y, duration=0)

while True:
    sleep(1)
    random_int = randint(0,2)
    if random_int == 0:
        smoother_move(acc_pos)
        pyautogui.click()
    else:
        smoother_move(dec_pos)
        pyautogui.click()

