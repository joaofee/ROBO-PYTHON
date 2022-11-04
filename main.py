


import time
import pyautogui
import pyperclip

pyautogui.PAUSE = 2


pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(10)
pyautogui.write("twitter.com")
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.press('enter')

arquivo_escrito_em_tela = pyperclip.paste()

if arquivo_escrito_em_tela != "https://twitter.com/home":
    pyautogui.hotkey('alt' , 'f4')
    time.sleep(6)
else:
    pyautogui.press('space')


time.sleep(10)
pyautogui.click(x=441, y=631)
pyautogui.write("meu robo que escreveu isso 1")
time.sleep(1)
pyautogui.click(x=1200, y=397)


meu robo que escreveu isso 1