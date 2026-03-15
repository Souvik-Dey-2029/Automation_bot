import pyautogui as pya
import time

def open_notepad():
    pya.press("win")
    time.sleep(1)

    pya.write("notepad",interval=0.1)
    pya.press("enter")

    time.sleep(1)

    pya.write("Automation Started!",interval=0.2)
    pya.press("enter")