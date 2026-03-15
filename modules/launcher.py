import pyautogui as pya
import webbrowser as web
import time

def launch_environment():
    
    print("Launching Coding Environmment..............")

    pya.press("win")
    time.sleep(1)
    pya.write("Visual Studio Code",interval=0.1)
    pya.press("enter")
    time.sleep(3)

    pya.press("win")
    time.sleep(1)
    pya.write("Chrome",interval=0.1)
    pya.press("enter")
    time.sleep(3)

    web.open("https://chatgpt.com/")
    time.sleep(2)
    web.open("https://github.com/")