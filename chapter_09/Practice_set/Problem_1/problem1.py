# Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.

with open("poems.txt") as f:
    content=f.read()
    word="twinkle"
    if(word in content):
        print("Word is there")
    else:
        print("word is not there")