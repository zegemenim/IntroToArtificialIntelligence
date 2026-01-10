import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('titanic')
print(df.head(), "\n")

plt.subplot(1, 2, 1)
sns.boxplot(x='class', y='age', data=df)
plt.title('Age Distribution by Class')
plt.xlabel('Class')
plt.ylabel('Age')
plt.subplot(1, 2, 2)
sns.boxplot(x='class', y='fare', data=df)
plt.title('Fare Distribution by Class')
plt.xlabel('Class')
plt.ylabel('Fare')
plt.tight_layout()
plt.show()