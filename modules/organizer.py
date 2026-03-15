import os
import shutil


def organize_downloads():

    print("Organizing Downloads folder...")

    downloads_path = r"C:\Users\SOUVIK\Downloads"

    # File type categories
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "PDFs": [".pdf"],
        "Documents": [".docx", ".txt"],
        "Code": [".py", ".java", ".zip"]
    }

    moved_files = 0

    for item in os.listdir(downloads_path):

        item_path = os.path.join(downloads_path, item)

        # Skip folders
        if os.path.isdir(item_path):
            continue

        file_extension = os.path.splitext(item)[1].lower()

        for folder, extensions in file_types.items():

            if file_extension in extensions:

                target_folder = os.path.join(downloads_path, folder)

                # Create folder if it doesn't exist
                os.makedirs(target_folder, exist_ok=True)

                destination = os.path.join(target_folder, item)

                # Move file
                shutil.move(item_path, destination)

                print(f"Moved: {item} → {folder}")

                moved_files += 1
                break

    if moved_files == 0:
        print("Downloads already organized.")
    else:
        print(f"{moved_files} file(s) organized successfully.")