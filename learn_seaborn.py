import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('athlete_events.csv')
print(data.describe())

plt.scatter('Height', 'Weight', data=data)
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Height vs Weight Scatter Plot')
plt.show()
sns.set_style('whitegrid')
sns.scatterplot(x='Height', y='Weight', data=data, hue='Sex', style='Medal', size='Age')
plt.title('Height vs Weight Scatter Plot with Seaborn')
plt.show()

sns.set_style('darkgrid')
sns.lineplot(x='Height', y='Weight', data=data, hue='Sex')
plt.title('Height vs Weight Line Plot with Seaborn')
plt.show()

sns.set_style('white')
sns.displot(x='Height', data=data, hue='Sex')
plt.title('Height Distribution with Seaborn')
plt.xlabel('Height')
plt.ylabel('Frequency')
plt.show()

data.corr(numeric_only=True)
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap with Seaborn')
plt.show()

data = np.array([5,7,9,15,20,22,25,30,32,35,37,40,50,55,60,100])
plt.figure(figsize=(10,6))
sns.boxplot(y=data)
plt.title('Box Plot with Seaborn')
plt.ylabel('Values')
plt.grid(True)
plt.show()