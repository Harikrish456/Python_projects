import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import csv
import statistics
import plotly.figure_factory as ff
##from google.colab import files
import random as rd

##file_upload = files.upload()
df = pd.read_csv('population.csv')
data = df['population'].tolist()

mean = statistics.mean(data)
median = statistics.median(data)
standard_deviation = statistics.stdev(data)

##fig = px.scatter(df, x = 'World Share', y = 'population', color = 'country', size = 'Land Area (Km²)', title = 'Population vs World Share')
##fig.show()

data_set = []
def sampling_data(counter):
    for i in range(0, counter):
        rand_index = rd.randint(0, len(data) - 1)
        rand_value = data[rand_index]
        data_set.append(rand_value)
    ##return data_set

sampling_data(100)

mean_sampdata = statistics.mean(data_set)
median_sampdata = statistics.median(data_set)

fig_normaldist = ff.create_distplot([data_set], ['Sampled Data'], show_hist=True)
fig_normaldist.show()

print('The mean for the raw data --> \n', mean)
print('The mean for the sampled data --> \n', mean_sampdata)
print('The median for the raw data --> \n', median)
print('The median for the sampled data --> \n', median_sampdata)
print('There were no unique mode for raw data')

