import pandas as pd
import numpy as np 

df_1 = pd.read_csv("ffcheckendataset.csv")
df_2 = pd.read_csv("WFPCleaned.csv")

result = pd.merge(df_1, df_2,  how='left', left_on=['country','year','food'], right_on = ['country','year','food'])

result.to_csv("ffdubbelcheck.csv")