import pandas as pd

df = pd.read_csv("WFPVAM_FoodPrices_05-12-2017.csv", encoding="ISO-8859-1")

# verandert de kolomnamen
df.columns = ["country_id", "country", "region_id", "region", "city_id", "city", "food_id", "food", "network_id", "network", "type_id", "type", "unit_id", "unit_measure", "month", "year", "price", "commodity_source"]

# haalt de dollar tekens en hashtags uit de namen van regio's weg
# for region in df["region"]:
#     if "$" in region:
#         region = region.replace("$", " ")
#     elif "#" in region:
#         region = region.replace("#", " ")

df.loc[df.region_id == 0, "region"] = "Unknown"

#for price in data["price"]:

# df.loc[df.unit_id == 16, "price"] = "price"/45

df = df.groupby([df["unit_id"], df["unit_measure"]]).mean()

#df = df["price"].groupby([df["country"], df["food"], df["year"]]).mean().round(decimals=2)

df.to_csv("unit_id dictorany.csv")

print(df)
