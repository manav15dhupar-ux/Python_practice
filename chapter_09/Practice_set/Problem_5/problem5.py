# Repeat program 4 for a list of such words to be censored.

words=["Donkey","bad","ganda"]

with open("sensor.txt","r") as f:
    content=f.read()

for word in words:

    content=content.replace(word,"#"*len(word))

with open("sensor.txt","w") as f:
    content=f.write(content)
