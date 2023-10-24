import pandas as pd
df = pd.read_csv('dpi_detailed_ipdr-20200831_00.00.00_100000.csv', sep=';', header=None)
df['11'] = df.iloc[:, 8] + df.iloc[:, 9]
df_you = df[df.iloc[:, 6] == 'youtube']
df_you = df_you.groupby(df_you.iloc[:, 1]).agg({'11': 'sum'})
print(df_you.sort_values(by='11', ascending=False).head(5))
