def validate(text):
  with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read().split("\n")
    if(text in content):
      return true
