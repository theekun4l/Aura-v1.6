from SmartManager.scanner import folderAnalyzer
from pathlib import Path
import shutil

categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Code": [".py", ".cpp", ".js", ".html", ".css"]
}

def Organizer(path):
    a = folderAnalyzer(path)

    # extracting files addresses
    l = [file for i in a.values() for file in i]

    organizer = {}

    for file in l:
        ext = file.suffix.lower()

        for category, extensions in categories.items():
            if ext in extensions:
                organizer.setdefault(category, []).append(file)
                break
        else:
            organizer.setdefault("Unknown", []).append(file)

    return organizer

def unique_name(destination, file):
    new_file = destination / file.name
    count = 1

    while new_file.exists():
        new_file = destination / f"{file.stem}_{count}{file.suffix}"
        count += 1

    return new_file



def folder_creator(path):
    a = Path(path)
    categories = ['Images', 'Documents', 'Videos', 'Audio', 'Code','Unknown']
    for category in categories:
        p = a / category
        p.mkdir(exist_ok=True) #it will create folder if it doesn't exist

def file_mover(path):
    folder_creator(path)
    organizer = Organizer(path)
    a = Path(path)

    for category,files in organizer.items():
        destination = a / category
        for what in files:
            where = unique_name(destination, what)
            shutil.move(what, where)


if __name__ == '__main__':
   print(unique_name(Path(r"C:\Users\Kunal\Pictures\Screenshots"),Path("ui.png")))