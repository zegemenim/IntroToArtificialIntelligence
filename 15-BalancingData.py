import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils import resample
from imblearn.over_sampling import SMOTE

np.random.seed(42)
set1no= 900
set2no= 100
df1 = pd.DataFrame({
    'Feature1': np.random.normal(loc=0, scale=1, size=set1no),
    'Feature2': np.random.normal(loc=0, scale=1, size=set1no),
    'target': np.zeros(set1no)
})
df2 = pd.DataFrame({
    'Feature1': np.random.normal(loc=5, scale=1, size=set2no),
    'Feature2': np.random.normal(loc=5, scale=1, size=set2no),
    'target': np.ones(set2no)
})

df = pd.concat([df1, df2], ignore_index=True)
print(df)
print(df.target.unique(), "\n")
print(df.target.value_counts(), "\n")

df_majority = df[df.target == 0]
df_minority = df[df.target == 1]

df_minority_upsampled = resample(df_minority, replace=True, n_samples=len(df_majority), random_state=42)

df_balanced = pd.concat([df_majority, df_minority_upsampled])
print(df_balanced.target.value_counts(), "\n")

oversample = SMOTE()
X_resampled, y_resampled = oversample.fit_resample(df[['Feature1', 'Feature2']], df['target'])
oversampled_df = pd.concat([X_resampled, y_resampled], axis=1)
