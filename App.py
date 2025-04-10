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

df1 = df.sort_values('Count',ascending= False).reset_index(drop= True)
print(df1)
df1 = df[['Location','Count']].sort_values(by = 'Count',ascending= False).head(5)
df1['Percentage'] = (df1['Count'] * 100 /df1['Count'].sum()).__round__(2)
print(df1)

df1.plot(x = 'Location' , y='Count' , kind = 'pie' , labels = df1.Location , autopct = '%1.2f%%')
print(plt.show())
