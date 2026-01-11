import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('titanic')
print(df[['sex', 'class', 'embark_town']].isna().sum())
df = df.dropna(subset=['embark_town'])
df_onehot = pd.get_dummies(df, columns=['sex', 'class', 'embark_town'], drop_first=True)

#label encoder
le = LabelEncoder()
df_label = df.copy()
df_label['sex'] = le.fit_transform(df_label['sex'])
print(df_label[['sex']].head())

#ordinal encoder
ordinal_encoder = OrdinalEncoder(categories=[['Third', 'Second', 'First']])
df_ordinal = df.copy()
df_ordinal['class'] = ordinal_encoder.fit_transform(df_ordinal[['class']])
print(df_ordinal[['class']])

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
df.sex.value_counts().plot(kind='bar', title='Original Categorical', ax=axes[0])
df_label.sex.value_counts().plot(kind='bar', title='Label Encoded', ax=axes[1])
df_onehot.sex_male.value_counts().plot(kind='bar', title='One-Hot Encoded', ax=axes[2])
plt.tight_layout()
plt.show()