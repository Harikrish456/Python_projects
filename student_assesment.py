import pandas as pd
import plotly.graph_objects as pgo

df = pd.read_csv('studentdata.csv')
student1 = df.loc[df['student_id']=='TRL_xsl']
print(student1)

print(student1.groupby('level')['attempt'].mean())

##fig = pgo.Figure(pgo.Bar(x=['Level 1', 'Level 2', 'Level 3', 'Level 4'], y=student1.groupby('level')['attempt'].mean()))
fig = pgo.Figure(pgo.Bar(x=student1.groupby('level')['attempt'].mean(), y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],orientation='h' ))
fig.show()