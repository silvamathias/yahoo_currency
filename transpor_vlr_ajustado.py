import pandas as pd

df = pd.read_csv('df_adj.csv')
#pp = df.columns
tp = df['OIBR3.SA']

print(tp)
