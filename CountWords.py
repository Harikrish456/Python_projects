import random



sentence = input("Enter string")
print(sentence)

characterCount = 0
wordCount = 1

characters = len(sentence)
print(characters)

for i in sentence:
    characterCount = characterCount + 1
    if i == ' ':
        wordCount = wordCount + 1
 
print(wordCount)
print(characterCount)