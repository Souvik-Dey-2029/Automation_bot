from modules.opener import open_notepad
from modules.launcher import launch_environment
from modules.organizer import organize_downloads
from modules.monitor import monitor_downloads
from modules.screenshot_logger import screenshot_logger

import threading


def start_monitor():
    thread = threading.Thread(target=monitor_downloads)
    thread.start()


def start_screenshot():
    thread = threading.Thread(target=screenshot_logger)
    thread.start()


def run_full_automation():

    open_notepad()
    launch_environment()
    organize_downloads()

    start_monitor()
    start_screenshot()


while True:

    print("\nSMART AUTOMATION BOT\n")

    print("1 → Launch Coding Environment")
    print("2 → Organize Downloads")
    print("3 → Start Download Monitor")
    print("4 → Start Screenshot Logger")
    print("5 → Run Full Automation")
    print("0 → Exit\n")

    choice = input("Enter choice: ")

    if choice == "1":
        launch_environment()

    elif choice == "2":
        organize_downloads()

    elif choice == "3":
        start_monitor()

    elif choice == "4":
        start_screenshot()

    elif choice == "5":
        run_full_automation()

    elif choice == "0":
        print("Exiting bot...")
        break

    else:
        print("Invalid option")
