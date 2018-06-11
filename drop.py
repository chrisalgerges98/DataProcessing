import pandas as pd

df = pd.read_csv("out_2.csv")

df.count = df["count"].astype("int64")

df = df.drop(df[df.count < 5].index)

df.to_csv("out_3.csv")
