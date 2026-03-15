from modules.logger import log
import pyautogui as pya
from modules.config_loader import load_config
import os
import time
from datetime import datetime


config = load_config()

folder = config["screenshot_folder"]
interval = config["screenshot_interval"]


def screenshot_logger():

    os.makedirs(folder, exist_ok=True)
    print("Screenshot logger is getting started.......")

    while True:

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{folder}/screenshot_{timestamp}.png"
        screenshot = pya.screenshot()
        screenshot.save(filename)
        print(f"Screenshot saved: {filename}")
        log(f"Screenshot saved: {filename}")

        time.sleep(interval)