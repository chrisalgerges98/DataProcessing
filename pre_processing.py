import pandas as pd

df = pd.read_csv("WFPVAM_FoodPrices_05-12-2017.csv", encoding="ISO-8859-1")

df = df[df.adm1_id != 0]
df = df.assign()
