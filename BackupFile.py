import os 
import shutil
 
source = input('Enter your source folder: ')
destination = input('Enter your destination folder: ')

listOfFiles = os.listdir(source)
print(listOfFiles) 
source = source + '/'
destination = destination + '/'

for fileName in listOfFiles :
    print(fileName)
    shutil.move((source + fileName), destination)

path = 'Countfunction'
isExist = os.path.exists(path)
print(isExist)

print(os.system('date'))