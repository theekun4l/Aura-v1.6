from pathlib import Path

def folderAnalyzer(path):
    dic = {}
    folder = Path(path)

    for item in folder.rglob("*"):
        if item.is_file():
            dic.setdefault(item.parent.name, []).append(item.name)

    return dic




