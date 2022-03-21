import csv
import pandas as pd
import plotly.express as px
import math

with open('class1.csv', newline='') as f:
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
    a = int(number[1]) - mean(file_data)
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

fig = px.scatter(df,    x="Student Number",
                        y="Marks"
            )

fig.update_layout(shapes=[
    dict(
      type= 'line',
      y0= mean, y1= mean,
      x0= 0, x1= total_entries
    )
])

fig.update_yaxes(rangemode="tozero")

fig.show()