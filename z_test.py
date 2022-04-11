import statistics
from numpy import std
import pandas as pd 
import random as rd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('student_marks.csv')
data = df['Math_score'].tolist()

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
    ##fig = ff.create_distplot([mean_set], ['mean_set'], show_hist=True)
    ##fig.show()
    print('Mean of sampled data --> \n', mean_of_mean)
    print('Standard deviation of sampled data --> \n', std_mean)

main()
mean_data = statistics.mean(data)
print('Mean of raw data --> \n', mean_data)
std_data = statistics.stdev(data)
print('Standard deviation of raw data --> \n', std_data)
##fig_2 = ff.create_distplot([data], ['data'], show_hist=True)
##fig_2.show()
first_std_start, first_std_end = mean_data - std_data, mean_data + std_data
second_std_start, second_std_end = mean_data - (2*std_data), mean_data + (2*std_data)
third_std_start, third_std_end = mean_data-(3*std_data), mean_data+(3*std_data)






school_1 = pd.read_csv('school_1.csv')
data_1 = school_1['Math_score'].tolist()
mean_of_school_1 = statistics.mean(data_1)
z_score_1 = (mean_data - mean_of_school_1)/std_data
print('Z score of school 1 --> \n', z_score_1)
print(mean_of_school_1)
fig = ff.create_distplot([data_1], ['Students who used the app'], show_hist=True)
fig.add_trace(go.Scatter(x=[mean_of_school_1, mean_of_school_1], y=[0, 0.17], mode="lines", name="Mean"))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

school_2 = pd.read_csv('school_2.csv')
data_2 = school_2['Math_score'].tolist()
mean_of_school_2 = statistics.mean(data_2)
z_score_2 = (mean_data - mean_of_school_2)/std_data
print('Z score of school 2 --> \n', z_score_2)
print(mean_of_school_2)
fig_2 = ff.create_distplot([data_2], ['Students who used '], show_hist=True)
fig_2.add_trace(go.Scatter(x=[mean_of_school_2, mean_of_school_2], y=[0, 0.17], mode="lines", name="Mean"))
fig_2.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig_2.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig_2.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig_2.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig_2.show()

school_3 = pd.read_csv('school_3.csv')
data_3 = school_3['Math_score'].tolist()
mean_of_school_3 = statistics.mean(data_3)
z_score_3 = (mean_data - mean_of_school_3)/std_data
print('Z score of school 3 --> \n', z_score_3)
print(mean_of_school_3)
fig_3 = ff.create_distplot([data_3], ['school 3'], show_hist=True)
fig_3.add_trace(go.Scatter(x=[mean_of_school_3, mean_of_school_3], y=[0, 0.17], mode="lines", name="Mean"))
fig_3.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig_3.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig_3.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig_3.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig_3.show()


