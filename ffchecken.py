import pandas as pd
import numpy as np 


# df_1 = pd.read_csv("AverageRateOfChange.csv")
# df_2 = pd.read_csv("YearlyRefugees.csv")

# result = pd.merge(df_1, df_2,  how='left', left_on=['Country','Year'], right_on = ['Country','Year'])

# result.to_csv("RateOfChangexRefugees.csv")





df_1 = pd.read_csv("RateOfChangexRefugees.csv")

result = df_1.groupby('Country')[['Rate_of_change_price','Rate_of_change_refugees']].corr()
result.to_csv("Correlation.csv")

