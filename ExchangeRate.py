import pandas as pd

df = pd.read_csv("MonthlyExchangeRate.csv")

df_1 = df.ix[:, 0:9]

df_2 = df.ix[:, 2529:2721]

df_3 = pd.concat([df_1, df_2], axis=1)

df_3 = df_3.drop(df_3[(df.Frequency == "Quarterly") | (df.Frequency == "Annual")].index)
df_3 = df_3.drop(df_3[df.Collection == "End of period"].index)

df_3.to_csv("test.csv")
