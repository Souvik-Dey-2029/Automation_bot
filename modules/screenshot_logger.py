from modules.logger import log
import pyautogui as pya
import os
import time
from datetime import datetime

def screenshot_logger():
    folder="SS"
    os.makedirs(folder,exist_ok=True)
    print("Screenshot logger is getting started.......")
    time.sleep(3)
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{folder}/screenshot_{timestamp}.png"
        screenshot = pya.screenshot()
        screenshot.save(filename)
        print(f"Screenshot saved: {filename}")
        log(f"Screenshot saved: {filename}")
        time.sleep(60)