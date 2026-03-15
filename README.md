# Smart Automation Bot 🤖

Smart Automation Bot is a modular Python automation toolkit that automates common desktop tasks like organizing downloads, monitoring files, capturing screenshots, and launching a coding environment.

---

## 🚀 Features

• Coding environment launcher
• Smart downloads organizer
• Automatic download monitoring
• Screenshot logger with timestamps
• Automation event logging
• Configurable settings using `config.json`
• CLI command system
• Multithreaded automation system

---

## 📁 Project Structure

```
Automation_bot
│
├── main.py
├── config.json
├── requirements.txt
│
├── logs
│   └── automation_log.txt
│
└── modules
    ├── opener.py
    ├── launcher.py
    ├── organizer.py
    ├── monitor.py
    ├── screenshot_logger.py
    ├── logger.py
    └── config_loader.py
```

---

## ⚙️ Installation

Clone the repository

```
git clone https://github.com/yourusername/smart-automation-bot.git
cd smart-automation-bot
```

Install dependencies

```
pip install -r requirements.txt
```

Run the bot

```
python main.py
```

---

## 🧠 Configuration

Edit **config.json** to customize the automation behavior.

Example:

```
{
  "downloads_folder": "C:\\Users\\YourName\\Downloads",
  "screenshot_interval": 60,
  "monitor_interval": 10,
  "screenshot_folder": "screenshots"
}
```

---

## 📝 Example Logs

```
[2026-03-16 00:20:11] Automation bot started
[2026-03-16 00:20:40] Screenshot saved
[2026-03-16 00:21:05] New file detected
[2026-03-16 00:21:05] Moved file example.pdf to PDFs
```

---

## 🛠 Technologies Used

Python
PyAutoGUI
Multithreading
JSON configuration
File automation

---

## 👨‍💻 Author

Souvik — CSE (AI & ML) student learning automation and backend development.
