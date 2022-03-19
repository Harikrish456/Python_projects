import shutil
import os
import time

data = time.time()
path = input('Enter your path name: ')

ctime = os.stat(path).st_ctime
print(ctime)

print(os.path.exists(path))

if os.path.exists(path):
    print(os.walk(path))
else :
    print('This file does not exist')

print(data)
print(os.path.isfile(path))

if ctime > data and os.path.isfile(path):
    print('if loop 1')
    os.remove(path)
    print('File removed succesfully')
elif ctime > data and os.path.isdir(path):
    shutil.rmtree(path)
    print('Folder succesfully removed')
else :
    print('This file is relatively new, we do not want to delete it')
