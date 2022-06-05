import csv
import pandas as pd
import math

with open('sd_data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

total_marks = 0
total_entries = len(file_data)

for marks in file_data:
    total_marks += float(marks[1])

mean = total_marks / total_entries
print("Mean (Average) is -> "+str(mean))


squared_list= []
for number in file_data:
    a = float(number[1]) - mean
    a= a**2
    squared_list.append(a)

sum =0
for i in squared_list:
    sum =sum + i
#dividing the sum by the total values
result = sum/ (len(file_data)-1)
std_deviation = math.sqrt(result)
print(std_deviation)


df = pd.read_csv("class1.csv")