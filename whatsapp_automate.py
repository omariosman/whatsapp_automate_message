import pandas as pd
import webbrowser
import pyautogui as pg
import time


message = "This is sent using python script"

url="https://web.whatsapp.com/send?phone=+201010352526&text=This is sent using python script"

webbrowser.open(url)


pg.press('enter')
time.sleep(5)
pg.press('ctrl')
time.sleep(3)
pg.keyDown('enter')

