import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression 

#Scatter plot
df = pd.read_csv('escape_velocity.csv')
scatter = px.scatter(df, x='Velocity', y='Escaped')
scatter.show()

#line of best fit
velocity_data = df['Velocity'].tolist()
escaped_data = df['Escaped'].tolist()

velocity_array = np.array(velocity_data)
escaped_array = np.array(escaped_data)

m,c = np.polyfit(velocity_array, escaped_array, 1)
print('value of m/c -->', m)
prebuild_y = []
for x in velocity_array:
    y_value = m*x + c
    prebuild_y.append(y_value)

prebuild_scatter = px.scatter(x=velocity_array, y = escaped_array) 
prebuild_scatter.update_layout(shapes = [
    dict(type = 'line', 
    y0 = min(prebuild_y), y1 = max(prebuild_y), 
    x0 = min(velocity_array), x1 = max(velocity_array)
    )
])
prebuild_scatter.show()

X = np.reshape(velocity_data, (len(velocity_data), 1))
Y = np.reshape(escaped_data, (len(escaped_data), 1))

lr = LogisticRegression()
lr.fit(X, Y)

plt.figure()
plt.scatter(X.ravel(), Y, color = 'black', zorder = 20)

def model(x):
    return 1/(1 + np.exp(-x))

#Line formula
X_test = np.linspace(0,100,200)
chances = model(X_test * lr.coef_ + lr.intercept_).ravel()

plt.plot(X_test, chances, color = 'red', linewidth = 3)
plt.axhline(y=0, color = 'k', linestyle = '-')
plt.axhline(y=1, color = 'k', linestyle = '-')
plt.axhline(y=0.5, color = 'k', linestyle = '-')

#hit and trial method 
plt.axvline(x = X_test[23], color = 'b', linestyle = '--')

plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(0,30)
plt.show()

user_score = 120
chances = model(user_score * lr.coef_ + lr.intercept_).ravel()[0]
if chances <= 0.01:
    print('will not escape')
elif chances >=1:
    print('will accepted')
elif chances < 0.5:
    print('might not escape')
else:
    print('may escape')