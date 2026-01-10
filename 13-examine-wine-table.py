import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('13-WineQT.csv')
print(df.head(), "\n")
sns.boxplot(x='quality', y='alcohol', data=df)
plt.title('Alcohol Content by Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Alcohol Content')
plt.show()
sns.boxplot(x='quality', y='pH', data=df)
plt.title('pH Level by Wine Quality')
plt.xlabel('Quality')
plt.ylabel('pH Level')
plt.show()
sns.boxplot(x='quality', y='sulphates', data=df)
plt.title('Sulphates Level by Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Sulphates Level')
plt.show()
sns.boxplot(x='quality', y='density', data=df)
plt.title('Density Level by Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Density Level')
plt.show()
sns.boxplot(x='quality', y='residual sugar', data=df)
plt.title('Residual Sugar Level by Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Residual Sugar Level')
plt.show()

columns = df.columns
(fig, axes) = plt.subplots(4,4, figsize=(15,15))
for i, column in enumerate(columns):
    sns.kdeplot(data=df, x=column, hue=df.quality, ax=axes.flatten()[i])
    axes.flatten()[i].set_title(f'Distribution of {column} by Quality')

plt.tight_layout()
plt.show()

for i in range(i+1, len(axes.flatten())):
    axes.flatten()[i].axis('off')