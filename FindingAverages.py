from collections import Counter
import csv 
import pandas as pd

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

listData = list(newData)

list = counterData.items()

def mode(list_of_nums):
    max_count = (0,0)
    for num in list_of_nums:
        occurrences = list_of_nums.count(num)
        if occurrences > max_count[0]:
            max_count = (occurrences, num)
    return max_count[1]

print(mode(listData))


##trying to find mode##

##for height, occurrence in counterData.items():
    ##if 50 < float(height) <60:
        ##mode_data_for_range["50-60"] += occurrence
   ## elif 60 < float(height) < 70:
       ## mode_data_for_range["60-70"] += occurrence
  ##  elif 70 < float(mode_data_for_range) < 80:
    ##    mode_data_for_range["70-80"] += occurrence

##mode_range, mode_occurence = 0,0
##for range, occurrence in mode_data_for_range.items():
    ##if occurrence > mode_occurence:
       ## mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1]), occurrence]

