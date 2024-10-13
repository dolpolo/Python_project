# IMPORT PANDA: library used for data-handling. (data cleaning and analysis)
# IMPORT COPY: library that provides functions for creating copies of objects. (modify an object withou affecting the original)
import pandas as pd
import copy as cp
import numpy as np

# Create DataFrames (use dictionaries, arrays, lists and lists of tuple)

df_dic=pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(df_dic)

df_arr=pd.DataFrame(np.array([[1,2],[3,4]]), index=["wow", "owo"], columns=["Yes", "No"])
print(df_arr)
df_arr.loc["wow","Yes"]=9
print(df_arr)
df_arr.iloc[0,1]=8
print(df_arr)

df_arr1=pd.DataFrame(np.array([(1,2),(3,4)]), index=["wow", "owo"], columns=["Yes", "No"])
print(df_arr1)

df_lst=pd.DataFrame([[1,2],[3,4]], index=["wow", "owo"], columns=["Yes", "No"])
print(df_lst)

df_tup=pd.DataFrame([(1,2),(3,4)], index=["wow", "owo"], columns=["Yes", "No"])
print(df_tup)

#Create Series (columns of a DataFrame)

sr_dic= pd.Series({"wow": 1, "owo": 2}, index= ["wow","owo"]) #index is useless
print(sr_dic)

sr_lst= pd.Series([1,2,3,4],index=["a","b","c","d"], name='Product A')
print(sr_lst)
sr_lst.iloc[1:3]=[5,6]
print(sr_lst)
sr_lst.loc["a"]=9
print(sr_lst)

# IMPORT A DATASET: from a file to a dataframe

# from a .csv file
beers = pd.read_csv("/Users/Davide/Desktop/Alma Mater/SECOND YEAR/PYTHON/Python_project/data/beers/beers.csv", delimiter=',')
print(beers.shape)
beers.head(6)
beers.describe
beers.rename(columns = {'Unnamed: 0': 'idx'}, inplace=True)
beers.set_index("idx", inplace=True) #inplace = TRUE to set the DataFrame index (row labels) using one existing column
# beers = beers.rename(columns = {'style': 'styles'}) use it to create relace the existing dataset 
beers.rename(columns = {'style': 'styles'}, inplace=True)#replace just the existing column with another name
beers.head()

# from .xlsx file