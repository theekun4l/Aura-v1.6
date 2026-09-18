from pathlib import Path

def folderAnalyzer(path):
    dic = {}
    folder = Path(path)

    for item in folder.rglob("*"):
        if item.is_file():
            dic.setdefault(item.parent.name, []).append(item.absolute())

    return dic
if __name__ == "__main__":
    a = folderAnalyzer(r"C:\Users\Kunal\Documents\Aura-v1.6")

    print(a)

