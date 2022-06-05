from statistics import mode
import pandas as pd
df = pd.read_csv('hwdata.csv', delimiter=';', decimal=',') 
mode = df['Weight'].mode()
print('weight mode: {}'.format(mode))