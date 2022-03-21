from collections import Counter
import csv
from pstats import Stats 
import pandas as pd
import statistics

with open('hwdata.csv', newline = '') as f: 
 reader = csv.reader(f)
 fileData = list(reader)
 print('reader', reader)
 

newData = []
fileData.pop(0)
print(range(len(fileData)))

for i in range(len(fileData)): 
    num = fileData[i][2]
    newData.append(float(num))

n = len(newData)

total = 0
for j in newData:
    total = total + j
    
mean = total/n
print('mean is', mean)
newData.sort()
print(newData)

if n % 2 == 0:
    m1 = (newData[n//2])
    m2 = (newData[n//2 - 1])
    m = (m1 + m2)/2
    print(m)
else: 
    median = (newData[n//2])
    print(median)

counterData = Counter(newData)
print(counterData)

## my own code to find mode ##

listData = list(newData)

list = counterData.items()

def mode(list_of_nums):
    max_count = (0,0)
    for num in list_of_nums:
        occurrences = list_of_nums.count(num)
        if occurrences > max_count[0]:
            max_count = (occurrences, num)
           
    print('occurence =',occurrences)
    if max_count[0] > 1:
        return max_count[1]     
    else:       
       print('no mode')
   

print(mode(listData))

mode2 = statistics.mode(newData)
print(mode2)

