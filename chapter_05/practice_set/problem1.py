# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words={
    "madad":"help",
    "billi":"cat",
    "meaze":"table"
}


word=input("Eneter the word to get meaning:")
print(words.get(word))
#or

# print(words[word])