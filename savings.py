from cv2 import mean
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

new_df = df[df['quant_saved'] < upper_whisker]
all_savings = new_df['quant_saved'].tolist()

print(f'Mean of revised savings - {statistics.mean(all_savings)}')
print(f'Mode of revised savings - {statistics.mode(all_savings)}')
print(f'Median of revised savings - {statistics.median(all_savings)}')
print(f'Standard deviation of revised savings - {statistics.stdev(all_savings)}')

fig_revised = ff.create_distplot([all_savings], ['Revised Savings Data'], show_hist=False)
fig_revised.show()
remained_df = new_df.loc[new_df['rem_any'] == 1]
not_remainded_df = new_df.loc[new_df['rem_any'] == 0]

fig_notrem = ff.create_distplot([not_remainded_df['quant_saved'].tolist()], ['Savings (not remainded)'], show_hist = False)
fig_notrem.show()

not_remainded_savings = not_remainded_df['quant_saved'].tolist()


sampling_mean_list_not_remainded = []
for i in range(1000):
    temp_list = []
    for j in range(100):
        temp_list.append(random.choice(all_savings))
    sampling_mean_list_not_remainded.append(statistics.mean(temp_list))

mean_sampling_not_remainded = statistics.mean(sampling_mean_list_not_remainded)
stdev_sampling_not_remainded = statistics.stdev(sampling_mean_list_not_remainded)
fig_sampmean = ff.create_distplot([sampling_mean_list_not_remainded], ['Sampled Savings List '], showhist=False)
fig_sampmean.add_trace(go.Scatter(x = [mean_sampling_not_remainded, mean_sampling_not_remainded], y = [0,0.1], mode='lines', name = 'mean'))
fig_sampmean.show()

print(f'Mean of sampling (not remainded) - {mean_sampling_not_remainded}')
print(f'The standarddeviation of the sampling (not remainded) - {stdev_sampling_not_remainded}')

not_remainded_savings = remained_df['quant_saved'].tolist()


sampling_mean_list_remainded = []
for i in range(1000):
    temp_list = []
    for j in range(100):
        temp_list.append(random.choice(all_savings))
    sampling_mean_list_remainded.append(statistics.mean(temp_list))

mean_sampling_remainded = statistics.mean(sampling_mean_list_remainded)
stdev_sampling_remainded = statistics.stdev(sampling_mean_list_remainded)
fig_sampmean_2 = ff.create_distplot([sampling_mean_list_remainded], ['Sampled Savings List '], showhist=False)
fig_sampmean_2.add_trace(go.Scatter(x = [mean_sampling_remainded, mean_sampling_remainded], y = [0,0.1], mode='lines', name = 'mean'))
fig_sampmean_2.show()

print(f'Mean of sampling (not remainded) - {mean_sampling_remainded}')
print(f'The standarddeviation of the sampling (not remainded) - {stdev_sampling_remainded}')

print(f'Standard deviation of sampled mean - {statistics.stdev(sampling_mean_list_remainded)}')
print(f'Mean of raw data - {statistics.mean(all_savings)}')
##print(f'Mean of sampled distribution - {statistics.mean(mean_sampling)}')

z_score = (mean_sampling_remainded - mean_sampling_not_remainded) / stdev_sampling_not_remainded
print(f'z_score - {z_score}')

temp_df = new_df[new_df.age != 0 ]

age = temp_df['age'].tolist()
savings = temp_df['quant_saved'].tolist()

correlation = np.corrcoef(age, savings)
print(f'Correlation is - {correlation}')


first_std_deviation_start = mean_sampling_not_remainded-stdev_sampling_not_remainded
first_std_deviation_end = mean_sampling_not_remainded+stdev_sampling_not_remainded
print(f'first start - {first_std_deviation_start} and first end - {first_std_deviation_end}')

second_std_deviation_start = mean_sampling_not_remainded - (2*stdev_sampling_not_remainded)
second_std_deviation_end = mean_sampling_not_remainded + (2*stdev_sampling_not_remainded)
print(f'second start - {second_std_deviation_start} and second end - {second_std_deviation_end}')

third_std_deviation_start = mean_sampling_not_remainded - (2*stdev_sampling_not_remainded)
third_std_deviation_end = mean_sampling_not_remainded + (2*stdev_sampling_not_remainded)
print(f'third start - {third_std_deviation_start} and third end - {third_std_deviation_end}')



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
    



