import pandas as pd
df = pd.read_csv('dpi_detailed_ipdr-20200831_00.00.00_100000.csv', sep=';', header=None)
df['11'] = df.loc[:, 8] + df.loc[:, 9]
df_new = df.groupby(df.loc[:, 6]).agg({'11': 'sum'})
print(df_new.sort_values(by='11', ascending=False).head(5))