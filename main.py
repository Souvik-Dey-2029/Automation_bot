from modules.opener import open_notepad
from modules.launcher import launch_environment
from modules.organizer import organize_downloads
from modules.monitor import monitor_downloads
from modules.screenshot_logger import screenshot_logger

import threading

print("Smart Automation is getting Started................\n")

# intial setup
open_notepad()
launch_environment()
organize_downloads()

# creating Threads
download_thread = threading.Thread(targent=monitor_downloads)
Screenshot_thread = threading.Thread(targent=screenshot_logger)

# Starting Threads
download_thread.start()
Screenshot_thread.start()