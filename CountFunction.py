def CountWordsFromFile():
    print('Hello')
    fileName = input("Enter the name of your file: ")
    numberOfWords = 0
    file = open(fileName, 'r')
    print(file)
    for line in file:
        print(line)
        words = line.split(',')
        numberOfWords = numberOfWords + len(words)
        print(len(words))
    print(numberOfWords)  
CountWordsFromFile()