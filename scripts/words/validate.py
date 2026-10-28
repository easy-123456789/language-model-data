def validate(text):
    path = "DATA/words/oxford-5000.txt"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read().splitlines()
    return text in content
