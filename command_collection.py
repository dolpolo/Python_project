# PANDA: library used for data-handling. (data cleaning and analysis)
# COPY: library that provides functions for creating copies of objects. (modify an object withou affecting the original)
import pandas as pd
import copy as cp

df=pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(df)

