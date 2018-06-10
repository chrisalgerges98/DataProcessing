import pandas as pd

df = pd.read_csv("out.csv")

df.columns = ["country", "food", "year", "average_price"]

df = df["year"].groupby([df["food"], df["country"]]).count()

df.to_csv("out_2.csv")
