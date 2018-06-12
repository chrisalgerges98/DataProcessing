import pandas as pd

df = pd.read_csv("WFPAveragePriceCleaned")

print(df["food"].unique())
