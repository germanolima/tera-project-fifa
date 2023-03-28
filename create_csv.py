#%%
import pandas as pd

df = pd.read_csv("C:/Users/Germano/Documents/tera-project-fifa/base/base.csv", low_memory=False)

df = df[df['ano']==22]

df_22 = pd.read_csv("C:/Users/Germano/Documents/tera_project/archive/players_22.csv", low_memory=False)

df = pd.merge(df, df_22, how='left', left_on=['sofifa_id', 'short_name'], right_on=['sofifa_id', 'short_name'])

df.to_csv("C:/Users/Germano/Documents/tera-project-fifa/base/base_bi.csv")
#%%