import os
from datetime import datetime


def log(message):

    os.makedirs("logs", exist_ok=True)

    log_file = "logs/automation_log.txt"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = f"[{timestamp}] {message}\n"

    with open(log_file, "a") as file:
        file.write(entry)