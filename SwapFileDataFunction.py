def SwapFileData(fileName, fileName2):
    print('Hello')
    nameOfFile1 = fileName + '.readme'
    nameOfFile2 = fileName2 + '.readme'
    file1 = open(nameOfFile1,'r')
    data1 = file1.read()
    
    file2 = open(nameOfFile2, 'r')
    data2 = file2.read()

    file1 = open(nameOfFile1, 'w')
    file1.write(data2)

    file2 = open(nameOfFile2, 'w')
    file2.write(data1)

    print('Data successfully swapped!')

    
    