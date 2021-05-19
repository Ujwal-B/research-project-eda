import pandas as pd
from pandas_profiling import ProfileReport
df=pd.read_csv('list1-modified.csv')
print(df)
profile = ProfileReport(df)
profile.to_file(output_file="analyse4.html")