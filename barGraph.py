import pandas as pd
import plotly.express as px 

df = pd.read_csv('data.csv')
print(df)
fig = px.line(df, x = 'Country', y = 'InternetUsers')
fig.show()