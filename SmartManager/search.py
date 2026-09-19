from SmartManager.scanner import folderAnalyzer

def search(path,desired):
    dic = folderAnalyzer(path)
    results = []
    for category, files in dic.items():
        for file in files:
            if desired.lower() in file.name.lower():
                results.append(file)

    return results