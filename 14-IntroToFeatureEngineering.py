import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('titanic')
print(df.isnull().sum(), "\n")
df.age.fillna(df.age.median(), inplace=True)
print(df.isnull().sum(), "\n")
df.dropna(subset=['embark_town'], inplace=True)
print(df.isnull().sum(), "\n")
mode_value = df[df["embarked"].notna()]["embarked"].mode()[0]
df['embarked'].fillna(mode_value, inplace=True)
print(df.isnull().sum(), "\n")