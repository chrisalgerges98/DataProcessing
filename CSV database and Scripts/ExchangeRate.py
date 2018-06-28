import pandas as pd

# reads necessary data
df_1 = pd.read_csv("WFPCleaned.csv")
df_2 = pd.read_csv("AnnualExchangeRate.csv")

# changes datatype to a float
df_2.Rate.astype("float64")

# drops the rows from the exchange rate dataset by countries,
# where the currency in the WFP Food Prices dataset is in USD
df_2 = df_2.drop(df_2[(df_2.Country == "Costa Rica") | (df_2.Country == "El Salvador")].index)
df_2 = df_2.drop(df_2[(df_2.Country == "Honduras") | (df_2.Country == "Panama") | (df_2.Country == "Zimbabwe")].index)

# creates a list of countries
Countries = df_1["country"].unique()

# checks whether the
df_2 = df_2[df_2["Country"].isin(Countries)]

print(len(Countries))
print(len(df_2["Country"].unique()))

# get the necessary values by index
df_1 = df.ix[:, 0:9]
df_2 = df.ix[:, 2947:2963]

# merge the two dataframes together
df_3 = pd.concat([df_1, df_2], axis=1)

# drops all Monthly and Quarterly exchange rates
# it also drops the exchange rate at the end of an period
df_3 = df_3.drop(df_3[(df.Frequency == "Quarterly") | (df.Frequency == "Monthly")].index)
df_3 = df_3.drop(df_3[df.Collection == "End of period"].index)

# (over)writes the preprocessed data to an csv file
df_2.to_csv("AnnualExchangeRate.csv")
