import pyautogui
import time
message = 100
while message > 0:
    time.sleep(2)
    pyautogui.typewrite("Ei Khankir pola tor maire chudi, madarchod, bessha magir beta")
    time.sleep(2)
    pyautogui.press('enter')
    message = message - 1


