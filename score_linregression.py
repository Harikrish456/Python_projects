import pandas as pd
import plotly.express as px
import numpy as np
#Was not able to find the perfect m, c in trial-and-error method

#Plotting a scatter plot
df = pd.read_csv('score_data.csv')
scatter = px.scatter(df, x='TOEFL', y='Chance of admit')
scatter.show()

#y = mx + c
m = 1
c = 0
y = []
toefl_data = df['TOEFL'].tolist()
chanceofadmit_data = df['Chance of admit'].tolist()

for x in toefl_data:
    value = m*x + c
    y.append(value)

#Linear regression
scatter.update_layout(shapes = [
    dict(type = 'line',
    y0 = min(y), y1 = max(y), 
    x0 = min(toefl_data), x1 = max(toefl_data)
    )
])

#Calculating chance of admit from toefl score
x_input = int(input('enter toefl score: '))
y_output = m*x + c
print(f'Someone with the toefl score of {x_input} will have a chance of admit of {y_output}')

#Finding slope and intercept from pre-defined computer algorithm
toefl_array = np.array(toefl_data)
admit_array = np.array(chanceofadmit_data)

m_new,c_new = np.polyfit(toefl_array, admit_array, 1)
print('value of m/c -->', m_new)
prebuild_y = []
for x in toefl_array:
    y_value = m_new*x + c_new
    prebuild_y.append(y_value)

algorithm_scatter = px.scatter(x=toefl_array, y = admit_array) 
algorithm_scatter.update_layout(shapes = [
    dict(type = 'line', 
    y0 = min(prebuild_y), y1 = max(prebuild_y), 
    x0 = min(toefl_array), x1 = max(admit_array)
    )
])
algorithm_scatter.show()

##Calculating weight and height using algroithm
x_input2 = int(input('enter toefl score (accurte version): '))
y_output2 = m_new*x + c_new
print(f'Someone with the toefl score of {x_input2} will have a chance of admit of {y_output2}')