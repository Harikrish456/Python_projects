
import time 

startTime = time.time()
def countWords():
 sentence = input("Enter string: ")
 print(sentence)

 searchRequest = input("Enter the letter you would like to search: ")

 characterCount = 0
 wordCount = 0

 for i in sentence:
    characterCount = characterCount + 1
    if i == searchRequest:
        wordCount = wordCount + 1
 
 print('number of times', searchRequest, 'appeared was', wordCount)
 print(characterCount)

def main():
    while (True):
        currecntTime = time.time() - startTime
        if(currecntTime >= 0):
            countWords
        
main()
