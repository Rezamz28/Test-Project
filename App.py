import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df = pd.read_csv('homicide_by_countries.csv')
print(df)
print(df.shape)
print(df.isnull().sum())
df.dropna(inplace=True)
df['Rate'] = df['Rate'].astype(int)
print(df)

my_list = ['Rate','Count','Year']
for i in my_list:
    df[i] = df[i].astype(int)

print(df)