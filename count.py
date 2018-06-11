import pandas as pd

df = pd.read_csv("out.csv")

df = df["year"].groupby([df["country"], df["food"]]).count()

df.to_csv("out_2.csv")
