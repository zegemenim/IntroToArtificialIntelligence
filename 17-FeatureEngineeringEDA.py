import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("17-googleplaystore.csv")
print(df.head())
print(df.info())

#  missing values
print(df.isnull().sum())

print(df["Reviews"].str.isnumeric().sum())
print(df[~df["Reviews"].str.isnumeric()])

df_clean = df.copy()
df_clean = df_clean[df_clean["Reviews"].str.isnumeric()]
df_clean["Reviews"] = df_clean["Reviews"].astype(int)
print(df_clean["Reviews"].dtype)
print(df_clean["Reviews"].info())

# Convert 'Size' to numeric
print(df_clean.Size.unique())
print(df_clean.info)
# df_clean.Size = df_clean.Size.str.replace("M", "")
df_clean.Size = df_clean.Size.dropna()
print(df_clean.info)


def mb_to_kb(size):
    if size.endswith("M"):
        return float(size[:-1]) * 1000
    elif size.endswith("k"):
        return float(size[:-1])
    elif size == "Varies with device":
        return np.nan
    else:
        return float(size)


df_clean["Size"] = df_clean["Size"].apply(mb_to_kb)
# df_clean = df_clean.dropna(subset=["Size"])
print(df_clean["Size"])
df_clean["Size"] = df_clean["Size"].astype(float)
print(df_clean["Size"].unique())
print(df_clean.head())

df_clean["Installs"] = df_clean["Installs"].str.replace(",", "").str.replace("+", "").astype(int)
print(df_clean["Installs"].unique())

df_clean["Price"] = df_clean["Price"].str.replace("$", "").astype(float)
print(df_clean["Price"].unique())

# Date feature
print(df_clean["Last Updated"].head())
df_clean["Last Updated"] = pd.to_datetime(df_clean["Last Updated"])
df_clean['Day'] = df_clean['Last Updated'].dt.day
df_clean['Month'] = df_clean['Last Updated'].dt.month
df_clean['Year'] = df_clean['Last Updated'].dt.year
print(df_clean[['Last Updated', 'Day', 'Month', 'Year']].head())

df_clean = df_clean.drop_duplicates(subset=['App'], keep='first')
print(df_clean.info())

# EDA
numeric_features = [feature for feature in df_clean.columns if df_clean[feature].dtype != 'O']
categorical_features = [feature for feature in df_clean.columns if df_clean[feature].dtype == 'O']
print("Numeric Features:", numeric_features)
plt.figure(figsize=(18, 6))

for i in range(0, len(numeric_features)):
    plt.subplot(5, 3, i + 1)
    sns.kdeplot(x=df_clean[numeric_features[i]], fill=True)
    plt.title(f'Distribution of {numeric_features[i]}')
    plt.xlabel(numeric_features[i])
    plt.tight_layout()
plt.show()

df_cat_installs = (df_clean.groupby('Category')['Installs'].sum().sort_values(ascending=False)/1000000).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x='Installs', y='Category', data=df_cat_installs.reset_index())
plt.title('Top 10 Categories by Total Installs (in millions)')
plt.xlabel('Total Installs (millions)')
plt.ylabel('Category')
plt.show()
apps = ["GAME", "COMMUNICATION", "TOOLS", "PRODUCTIVITY", "SOCIAL"]
df_app_category = df_clean.groupby(['Category', 'App'])['Installs'].sum().reset_index()
df_app_category = (df_app_category.sort_values("Installs", ascending=False))

for i, app in enumerate(apps):
    df2 = df_app_category[df_app_category.Category == app].head(5)
    plt.subplot(3, 2, i + 1)
    sns.barplot(x='Installs', y='App', data=df2)
    plt.title(f'Top 5 Apps in {app}')
    plt.xlabel('Installs')
    plt.ylabel('App')
plt.tight_layout()
plt.show()

rating_df = df_clean.groupby(['Category', 'Installs', 'App'])['Rating'].sum().sort_values(ascending=False).reset_index()
print(rating_df, "\n")
df_clean['Android Ver'] = df_clean['Android Ver'].replace('and up', '', regex=True).replace('W', '', regex=True)
df_clean['Android Ver'] = df_clean['Android Ver'].replace('Varies with device', np.nan)
print(df_clean['Android Ver'].unique())
df_clean = df_clean[df_clean['Android Ver'].str.contains('-') == False]

mean_genres_installs = (df_clean.groupby('Genres')['Installs'].mean() / 100000).to_dict()
df_clean['Genres Encoded'] = df_clean['Genres'].map(mean_genres_installs)
print(df_clean[['Genres', 'Genres Encoded']].head())
