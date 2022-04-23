import plotly.express as px
import pandas as pd 
import numpy as np

##Plotting scatter graph
df = pd.read_csv('linear_regressiondata.csv')
scatter = px.scatter(df, x='Height', y = 'Weight')
scatter.show()

##Coding for 'y = mx + c'
m = 0.95
c = -93
y = []
height_data = df['Height'].tolist()
weight_data = df['Weight'].tolist()

for x in height_data:
    y_value = (m*x) + c
    y.append(y_value)
    
print('y -->', y)
print('height data -->', height_data)

##Plotting for linear regression
fig_scatter = px.scatter(x=height_data, y=weight_data)
fig_scatter.update_layout(shapes = [
    dict(type = 'line', 
    y0 = min(y), y1 = max(y), 
    x0 = min(height_data), x1 = max(height_data)
    )
    ])
fig_scatter.show()

#Calculating weight from height
x_input = int(input('What is the height?'))
y_output = m*x + c
print(f'Someone with the height {x_input} will have a weight of {y_output}')

#Finding slope and intercept from pre-defined computer algorithm
height_array = np.array(height_data)
weight_array = np.array(height_data)

m_new,c_new = np.polyfit(height_array, weight_array, 1)
print('value of m/c -->', m_new)
prebuild_y = []
for x in height_array:
    y_value = m_new*x + c_new
    prebuild_y.append(y_value)

prebuild_scatter = px.scatter(x=height_array, y = weight_array) 
prebuild_scatter.update_layout(shapes = [
    dict(type = 'line', 
    y0 = min(prebuild_y), y1 = max(prebuild_y), 
    x0 = min(height_array), x1 = max(height_array)
    )
])
prebuild_scatter.show()

##Calculating weight and height using algroithm
x_input2 = int(input('What is the height? This time, more accuarate'))
y_output2 = m_new*x + c_new
print(f'Someone with the height {x_input2} will have a weight of {y_output2}')

