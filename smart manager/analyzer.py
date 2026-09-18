from scanner import folderAnalyzer
from pathlib import Path

def format_size(size):
    if size < 1024**2:
        return f"{size / 1024:.2f} KB"
    elif size < 1024**3:
        return f"{size / 1024**2:.2f} MB"
    else:
        return f"{size / 1024**3:.2f} GB"

def Analyzer(folder):
    p = Path(folder)
    a = folderAnalyzer(folder)

    #extracting files addresses
    l = [file for i in a.values() for file in i]

    #folder names
    folder_names = [folder for folder in a if folder != p.name]

    if l:

    #calculating total size
        size = 0
        for f in l: size += f.stat().st_size

        extension = {}
        size_ext = {}
        for file in l:
            ext = file.suffix.lower()
            f_sz = file.stat().st_size
            extension[ext] = extension.setdefault(ext,0) + 1
            size_ext[ext] = size_ext.setdefault(ext,0) + f_sz

    #largest and smallest files
        largest = max(l, key=lambda file: file.stat().st_size)
        smallest = min(l, key=lambda file: file.stat().st_size)

        largest_file = {
            "name": largest.name,
            "size": format_size(largest.stat().st_size)
        }

        smallest_file = {
            "name": smallest.name,
            "size": format_size(smallest.stat().st_size)
        }

    else:
        extension = {}
        size_ext = {}
        largest_file = None
        smallest_file = None
        size = 0

    return {"total files": len(l),"total folders": len(folder_names),"extension": extension},{"total size":format_size(size),"extension wise size":size_ext},largest_file,smallest_file

if __name__ == "__main__":
    a,b,c,d= Analyzer("c:/users/Kunal/documents/Aura-v1.6/smart manager")
    print(a,b,c,d)