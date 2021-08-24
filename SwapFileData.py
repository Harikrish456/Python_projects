def SwapFileData():
    print('Hello')
    fileName = input('Enter your first file name: ')
    file1 = open(fileName,'r')
    data1 = file1.read()
    fileName2 = input('Enter your second file name: ')
    file2 = open(fileName2, 'r')
    data2 = file2.read()

    file1 = open(fileName, 'w')
    file1.write(data2)

    file2 = open(fileName2, 'w')
    file2.write(data1)
SwapFileData()
    
    