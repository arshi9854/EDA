# -*- coding: utf-8 -*-
"""zomato EDA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_Zumu0KNVZQ6KESeWIW54ZqrvMWvt8cw
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df=pd.read_csv('zomato.csv',encoding='latin-1')
df.head()

df.columns

df.info()

df.describe()

df.isnull().sum()

[features for features in df.columns if df[features].isnull().sum()>0]

df_country=pd.read_excel('Country-Code.xlsx')
df_country.head()

df.columns

final_df=pd.merge(df,df_country,on='Country Code',how='left')

final_df.head(2)

final_df.dtypes

final_df.Country.value_counts()

country_names=final_df.Country.value_counts().index

country_val=final_df.Country.value_counts().values

plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')

final_df.columns

ratings=final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating Count'})

ratings.head()

import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(x="Aggregate rating",y="Rating Count",data=ratings)

sns.barplot(x="Aggregate rating",y="Rating Count",hue='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])

sns.countplot(x="Rating color",data=ratings,palette=['blue','red','orange','yellow','green','green'])

final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index().head(5)

final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)

final_df.head()

final_df.columns

final_df.groupby(['Country','Currency']).size().reset_index()

final_df[final_df['Has Online delivery']=="Yes"].Country.value_counts()

final_df.groupby(['Country','Has Online delivery']).size().reset_index()

final_df.City.value_counts().index

city_values=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index

plt.pie(city_values[:5],labels=city_labels[:5],autopct='%1.2f%%')

final_df.columns

final_df.Cuisines.value_counts().index

Cuisines_values=final_df.Cuisines.value_counts().values
Cuisines_index=final_df.Cuisines.value_counts().index

plt.pie(Cuisines_values[:10],labels=Cuisines_index[:10],autopct='%1.2f%%')





