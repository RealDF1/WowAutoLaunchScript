import subprocess
import pyautogui
import time

class mouse:
    def Click():
        currentMouseX, currentMouseY = pyautogui.position()

        print(currentMouseX, currentMouseY)


        pyautogui.moveTo(450,880)
        pyautogui.click()

path = ("C:\Program Files (x86)\Battle.net\Battle.net Launcher") # Путь до лаунчера

battle_net_stert = subprocess.Popen(path)
battle_net_stert.poll()

currentMouseX, currentMouseY = pyautogui.position()

print(currentMouseX, currentMouseY)
time.sleep(10)
mouse.Click()

pyautogui.moveTo(450,880)
pyautogui.click()