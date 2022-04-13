import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import csv
import statistics

df = pd.read_csv('savings_data.csv')
##fig = px.scatter(df, x= 'quant_saved', y='rem_any', size = 'quant_saved', color = 'rem_any')
##fig.show()

with open('savings_data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

#To remove headers from CSV
file_data.pop(0)

total_len = len(file_data)
counter = 0

for data in file_data:
    if int(data[3]) == 1:
        counter = counter + 1

no_rem = total_len - counter
print('Number of people who received no remainders --> \n', no_rem)
print('Number of people who received a remainder --> \n', counter)

##figure = go.Figure(go.Bar(x=['remainded', 'not remainded'], y = [counter, no_rem]))
##figure.show()

remainded_savings = []
notremainded_savings = []

for i in file_data:
    if int(i[3]) == 1:
        remainded_savings.append(float(i[0]))
    else:
        notremainded_savings.append(float(i[0]))

print('rem', remainded_savings)
print('notrem', notremainded_savings)

print( 'The mean for the remainded savings --> \n',statistics.mean(remainded_savings))
print('The mean for the not remainded savings --> \n', statistics.mean(notremainded_savings))
print('The mode of the remainded savings --> \n',statistics.mode(remainded_savings))
print('The mode of the not remainded savings --> \n',statistics.mode(notremainded_savings))
print('The median of the remainded savings --> \n', statistics.median(remainded_savings))
print('The median of the not remainded savings --> \n', statistics.median(notremainded_savings))
print('The standard deviation of the remainded savings --> \n', statistics.stdev(remainded_savings))
print('The standard deviation of the not remainded savings --> \n', statistics.stdev(notremainded_savings))
    



