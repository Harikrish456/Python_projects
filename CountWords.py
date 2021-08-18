import random

number = random.randint(1,9)
print(number)

sentence = input("Enter string")
print(sentence)

characterCount = 0
wordCount = 1

for i in sentence:
    characterCount = characterCount + 1
    if i == ' ':
        wordCount = wordCount + 1
 
print(wordCount)
print(characterCount)