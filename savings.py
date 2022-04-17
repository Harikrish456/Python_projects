import numpy as np
import pandas as pd
import plotly.express as px
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go 
import csv
import statistics
import seaborn as sns

df = pd.read_csv('savings_data.csv')
distplot_data = df['quant_saved'].tolist()
fig = px.scatter(df, x= 'quant_saved', y='rem_any', size = 'quant_saved', color = 'rem_any')
fig.show()

sns.boxplot(data=df, x=df['quant_saved'])

q1 = df['quant_saved'].quantile(0.25)
q3 = df['quant_saved'].quantile(0.75)
iqr = q3 - q1

print(f'IQR - {iqr}')

lower_whisker = q1 + 1.5*iqr
upper_whisker = q3 + 1.5*iqr

print(f'Lower whisker - {lower_whisker}')
print(f'The upper whisker - {upper_whisker}')

revised_df = df[df['quant_saved'] < upper_whisker]
new_savings = revised_df['quant_saved'].tolist()

print(f'Mean of revised savings - {statistics.mean(new_savings)}')
print(f'Mode of revised savings - {statistics.mode(new_savings)}')
print(f'Median of revised savings - {statistics.median(new_savings)}')
print(f'Standard deviation of revised savings - {statistics.stdev(new_savings)}')

fig_revised = ff.create_distplot([new_savings], ['Revised Savings Data'], show_hist=False)
fig_revised.show()

sampling_mean_list = []
for i in range(1000):
    temp_list = []
    for j in range(100):
        temp_list.append(random.choice(new_savings))
    sampling_mean_list.append(statistics.mean(temp_list))

mean_sampling = statistics.mean(sampling_mean_list)
fig_sampmean = ff.create_distplot([sampling_mean_list], ['Sampled Savings List '], showhist=False)
fig_sampmean.add_trace(go.Scatter(x = [mean_sampling, mean_sampling], y = [0,0.1], mode='lines', name = 'mean'))
fig_sampmean.show()

print(f'Standard deviation of sampled mean - {statistics.stdev(sampling_mean_list)}')
print(f'Mean of raw data - {statistics.mean(new_savings)}')
##print(f'Mean of sampled distribution - {statistics.mean(mean_sampling)}')

temp_df = revised_df[revised_df.age != 0 ]

age = temp_df['age'].tolist()
savings = temp_df['quant_saved'].tolist()

correlation = np.corrcoef(age, savings)
print(f'Correlation is - {correlation}')

remained_df = revised_df.loc[revised_df['rem_any'] == 1]
notrem_df = revised_df.loc[revised_df['rem_any'] == 0]

fig_notrem = ff.create_distplot([notrem_df['quant_saved'].tolist()], ['Savings (not remainded)'], show_hist = False)
fig_notrem.show()



distplot_fig = ff.create_distplot([distplot_data], ['Quantity saved'], show_hist=True)
distplot_fig.show()

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

figure = go.Figure(go.Bar(x=['remainded', 'not remainded'], y = [counter, no_rem]))
figure.show()


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
    



