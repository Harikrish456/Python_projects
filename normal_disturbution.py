from numpy import count_nonzero
import pandas
import plotly.figure_factory as ff
import pandas as pd
import random

from scipy import rand 

count = []
diceResult = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1+dice2)
    count.append(i)
    
##print(count)
##fig = px.bar(x=diceResult, y=count)
##fig.show()

df = pd.read_csv('mobile_data.csv')
fig = ff.create_distplot([df['Avg Rating'].tolist()], ['Avg Rating'], show_hist=True)
fig.show()