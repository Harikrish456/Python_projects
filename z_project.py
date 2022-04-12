import statistics
from numpy import std
import pandas as pd 

import plotly.figure_factory as ff

import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
mean = statistics.mean(data)
stdev = statistics.stdev(data)

df_2 = pd.read_csv('z_project_data.csv')
data_2 = df_2['reading_time'].tolist()
mean_2 = statistics.mean(data_2)
z_score = (mean - mean_2)/stdev
print('Z score for reading time --> \n', z_score)

fig = ff.create_distplot([data_2], ['reading time'], show_hist=True)
fig.show()