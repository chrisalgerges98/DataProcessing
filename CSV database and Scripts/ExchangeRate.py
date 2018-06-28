import pandas as pd

df_1 = pd.read_csv("WFPCleaned.csv")
df_2 = pd.read_csv("AnnualExchangeRate.csv")
df_2.Rate.astype("float64")

# for price in df_1["average_price"]:
#     currency = df_1["currency"].loc[df_1["average_price"] == price]
#     year = df_1["year"].loc[df_1["average_price"] == price]

df_2 = df_2.drop(df_2[(df_2.Country == "Costa Rica") | (df_2.Country == "El Salvador")].index)
df_2 = df_2.drop(df_2[(df_2.Country == "Honduras") | (df_2.Country == "Panama") | (df_2.Country == "Zimbabwe")].index)

# Countries = df_1["country"].unique()
#
# df_2 = df_2[df_2["Country"].isin(Countries)]
#
# print(len(Countries))
# print(len(df_2["Country"].unique()))
#
# df_2.to_csv("AnnualExchangeRate.csv")

# df_1 = df.ix[:, 0:9]
#
# df_2 = df.ix[:, 2947:2963]
#
# df_3 = pd.concat([df_1, df_2], axis=1)
#
# df_3 = df_3.drop(df_3[(df.Frequency == "Quarterly") | (df.Frequency == "Monthly")].index)
# df_3 = df_3.drop(df_3[df.Collection == "End of period"].index)
