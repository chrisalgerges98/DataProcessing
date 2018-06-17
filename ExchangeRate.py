import pandas as pd

df_1 = pd.read_csv("WFPCleaned.csv")
df_2 = pd.read_csv("AnnualExchangeRate.csv")
# df_2.Rate.astype("float64")
# df_1["AveragePriceInUSD"] = df_1["average_price"] / df_2["Rate"]

Countries = df_1["country"].unique()

df_2 = df_2[df_2["Country"].isin(Countries)]

print(len(df_2["Country"].unique()))
print(len(Countries))

# df_2.to_csv("AnnualExchangeRate.csv")

# df_1 = df.ix[:, 0:9]
#
# df_2 = df.ix[:, 2947:2963]
#
# df_3 = pd.concat([df_1, df_2], axis=1)
#
# df_3 = df_3.drop(df_3[(df.Frequency == "Quarterly") | (df.Frequency == "Monthly")].index)
# df_3 = df_3.drop(df_3[df.Collection == "End of period"].index)
