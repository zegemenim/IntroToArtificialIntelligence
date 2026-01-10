import numpy as np
import pandas as pd

weather_df = pd.read_excel('6-weather.xlsx')
print(weather_df.head())
print(weather_df.describe())

# Working with missing data
weather_na_df = pd.read_excel('6-weatherna.xlsx')
print(weather_na_df, "\n")
print(weather_na_df.isna(), "\n")
print(weather_na_df.describe(), "\n")

# Group by

df = pd.read_csv('6-employee.csv')
print(df.head(), "\n")
print(df.describe(), "\n")
print(df['Experience'] > 6, "\n")
grouped_by_city = df.groupby('City')
print(grouped_by_city.describe(), "\n")

#concat and merge
df1 = pd.read_csv('7-concat_data1.csv')
df2 = pd.read_csv('7-concat_data2.csv')
print(df1.head, "\n")
print(df2.head, "\n")
concatenated_df = pd.concat([df1, df2], ignore_index=True)
print(concatenated_df, "\n")
# Merge dataframes
df1 = pd.read_csv('7-merge_data1.csv')
df2 = pd.read_csv('7-merge_data2.csv')
print(df1.head, "\n")
merged_df = pd.merge(df1, df2, on='Employee_ID', how='outer') # All records
print(merged_df, "\n")
merged_df_inner = pd.merge(df1, df2, on='Employee_ID', how='inner') # Only matching records
print(merged_df_inner, "\n")
merged_df_left = pd.merge(df1, df2, on='Employee_ID', how='left') # All records from df1
print(merged_df_left, "\n")
merged_df_right = pd.merge(df1, df2, on='Employee_ID', how='right') # All records from df2
print(merged_df_right, "\n")

# Apply function
df = pd.read_csv('8-apply_function_data.csv')
print(df.head(), "\n")

def add_performance_score(row):
    if row > 10:
        return 1
    else:
        return 0

df['New_Performance_Score'] = df["Performance_Score"] + df["Experience"].apply(add_performance_score)
print(df.head(), "\n")