from scanner import folderAnalyzer
from pathlib import Path

def format_size(size):
    if size < 1024**2:
        return f"{size / 1024:.2f} KB"
    elif size < 1024**3:
        return f"{size / 1024**2:.2f} MB"
    else:
        return f"{size / 1024**3:.2f} GB"

def Analyzer(f):
    p = Path(f)
    a = folderAnalyzer(f)
    #making list files addresses
    l = [p / folder / file for folder, files in a.items() for file in files]
    #calculating size of each file
    size = [f.stat().st_size for f in l]
    total = format_size(sum(size))
    extension = {}
    for file in l:
        ext = file.suffix.lower()
        extension[ext] = extension.setdefault(ext,0) + 1

    return l

a = Analyzer("c:/users/Kunal/documents/Aura-v1.6/smart manager")
print(a)