
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import random
import statistics
from scipy import rand 

df = pd.read_csv('StudentsPerformance.csv')

mean = sum(df['math score'])/len(df["math score"])
print('The median is --> \n', mean)
median = statistics.median(df["math score"])
print('The median is --> \n', median)
mode = statistics.mode(df["math score"])
print('The mode is --> \n', mode)
standard_deviation = statistics.stdev(df["math score"])
print('The standard deviation is --> \n', standard_deviation)

fig_2 = ff.create_distplot([df["math score"].tolist()], ['df'], show_hist = False)
fig_2.show()

first_std_start, first_std_end = mean - standard_deviation, mean + standard_deviation
second_std_start, second_std_end = mean - (2*standard_deviation), mean + (2*standard_deviation)
third_std_start, third_std_end = mean-(3*standard_deviation), mean+(3*standard_deviation)
#Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations

fig_2.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig_2.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig_2.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig_2.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig_2.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig_2.add_trace(go.Scatter(x=[third_std_end, third_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig_2.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig_2.show()
#Printing the findings
list_of_data_within_1_std_deviation = [result for result in df["math score"] if result > first_std_start and result < first_std_end]
list_of_data_within_2_std_deviation = [result for result in  df["math score"] if result > second_std_start and result < second_std_end]
list_of_data_within_3_std_deviation = [result for result in  df["math score"] if result > third_std_start and result < third_std_end]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(standard_deviation))
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len( df["math score"])))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len( df["math score"])))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len( df["math score"])))
    
##print(count)
##fig = px.bar(x=diceResult, y=count)
##fig.show()

##df = pd.read_csv('mobile_data.csv')
##fig = ff.create_distplot([df['Avg Rating'].tolist()], ['Avg Rating'], show_hist=True)
##fig.show()