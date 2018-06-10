import pandas as pd

df = pd.read_csv("WFPVAM_FoodPrices_05-12-2017.csv", encoding="ISO-8859-1")

# verandert de kolomnamen
df.columns = ["country_id", "country", "region_id", "region", "city_id", "city", "food_id", "food", "currency_id", "currency", "market_id", "market", "unit_id", "unit_measure", "month", "year", "price", "commodity_source"]

# haalt de dollar tekens en hashtags uit de namen van regio's weg
# for region in df["region"]:
#     if "$" in region:
#         region = region.strip("$")
#     elif "#" in region:
#         region = region.strip("#")
#     else:
#         continue

df.loc[df.region_id == 0, "region"] = "Unknown"

# df = df.groupby([df["unit_id"], df["unit_measure"]]).mean()

#df = df["price"].groupby([df["country"], df["food"], df["year"]]).mean().round(decimals=2)

# dropt irrelevante data
df = df.drop(df[(df.year < 2001) | (df.year > 2016)].index)
df = df.drop(df[df.food == "Exchange rate"].index)
df = df.drop(df[df.food == "Exchange rate (unofficial)"].index)
df = df.drop(df[df.food == "Wage (non-qualified labour)"].index)
df = df.drop(df[df.food == "Wage (non-qualified labour, agricultural)"].index)
df = df.drop(df[df.food == "Wage (non-qualified labour, non-agricultural)"].index)
df = df.drop(df[df.food == "Wage (qualified labour)"].index)
df = df.drop(df[df.food == "Transport (public)"].index)

# df = df.groupby(df["region"]).mean()

df.to_csv("region.csv")

print(df["region"])
