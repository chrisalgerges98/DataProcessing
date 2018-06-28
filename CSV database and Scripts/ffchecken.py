import pandas as pd
import numpy as np

# reads data from csv files
df_1 = pd.read_csv("AverageRateOfChange.csv")
df_2 = pd.read_csv("YearlyRefugees.csv")

# merges two dataframes by country and year
result = pd.merge(df_1, df_2,  how='left', left_on=['Country','Year'], right_on = ['Country','Year'])

# writes result to a csv file
result.to_csv("RateOfChangexRefugees.csv")

# reads data from to_csv
df_1 = pd.read_csv("RateOfChangexRefugees.csv")

# calculates the correlation between the rate of change of the price
# and the rate of change of the refugees
result = df_1.groupby('Country')[['Rate_of_change_price','Rate_of_change_refugees']].corr()
result.to_csv("Correlation.csv")
