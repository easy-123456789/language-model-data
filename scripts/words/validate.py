def validate(text):
  with open("DATA/words/oxford-5000.txt", "r", encoding="utf-8") as f:
    content = f.read().split("\n")
    if(text in content):
      return true
