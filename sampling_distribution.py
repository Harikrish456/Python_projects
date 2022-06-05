import statistics
from numpy import std
import pandas as pd 
import random as rd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('temp_averages.csv')
data = df['average'].tolist()

def random_mean(counter):
    data_set = []
    for i in range(0,counter):
        rand_index = rd.randint(0, len(data) - 1)
        rand_value = data[rand_index]
        data_set.append(rand_value)
    mean = statistics.mean(data_set)
    return mean

def main():
    mean_set = []
    rand_input = rd.randint(0,500)
    for i in range(0,1000):
      value = random_mean(rand_input)
      mean_set.append(value)
    mean_of_mean = statistics.mean(mean_set)
    std_mean = statistics.stdev(mean_set)
    fig = ff.create_distplot([mean_set], ['mean_set'], show_hist=True)
    fig.show()
    print('Mean of sampled data --> \n', mean_of_mean)
    print('Standard deviation of sampled data --> \n', std_mean)
    

    

main()
mean_data = statistics.mean(data)
print('Mean of raw data --> \n', mean_data)
std_data = statistics.stdev(data)
print('Standard deviation of raw data --> \n', std_data)
fig_2 = ff.create_distplot([data], ['data'], show_hist=True)
fig_2.show()

      
