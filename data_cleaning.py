import pandas as pd

df = pd.read_csv('5statesdata.csv')


df.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)


df_cleaned = df.dropna(how='all')


df_cleaned['Date'] = pd.to_datetime(df_cleaned['Date'])


df_cleaned = df_cleaned.sort_values(by='Date')


df_cleaned.to_csv('cleaned_5statesdata.csv', index=False)

print("Data cleaning for 5statesdata.csv completed.")
