# -*- coding: utf-8 -*-
"""Python and Data Analytics Project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17ARHETNRR3sXqe1BOMWq9hpVnngNjUb3
"""

import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_csv('/content/train.csv'))
df.head()

#df.shape

df.isnull().sum()

drop_col = df.isnull().sum()[df.isnull().sum()>(35/100 * df.shape[0])]
drop_col

drop_col.index

df.drop(drop_col.index, axis=1, inplace = True)
df.isnull().sum()

df.fillna(df.mean(), inplace = True)
df.isnull().sum()

df['Embarked'].describe()

df['Embarked'].fillna('S',inplace=True)

df.isnull().sum()

df.corr()

df['FamilySize'] = df['SibSp']+df['Parch']
df.drop(['SibSp', 'Parch'], axis=1 , inplace=True)
df.corr()

df['Alone'] = [0 if df['FamilySize'][i]>0 else 1 for i in df.index]
df.head()

df.groupby(['Alone'])['Survived'].mean()

df[['Alone','Fare']].corr()

df['Sex'] = [0 if df['Sex'][i]=='male' else 1 for i in df.index]
df.groupby(['Sex'])['Survived'].mean()

df.groupby(['Embarked'])['Survived'].mean()

"""CONCLUSION



*   Female passengers were prioritized over men.

*   People with high class or rich people have higher survival rate than others.Thr hierarichy might have been followed while saving the passangers.
*  Passangers travelling with their family have higher survival rate.


*   Passangers who borded the ship at Cherbourg,survived more in proportion then the others.






"""