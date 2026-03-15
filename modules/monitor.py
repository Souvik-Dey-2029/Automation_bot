from modules.logger import log
import os
import time
from modules.organizer import organize_downloads


def monitor_downloads():

    downloads_path = r"C:\Users\SOUVIK\Downloads"

    print("Download Monitor Started...")
    print("Watching for new files...\n")

    previous_files = set(os.listdir(downloads_path))

    while True:

        time.sleep(15)  # check every 10 seconds

        current_files = set(os.listdir(downloads_path))

        # detect new files
        new_files = current_files - previous_files

        if new_files:
            print("New file detected:", new_files)
            log(f"New file detected: {new_files}")
            organize_downloads()

        previous_files = current_files