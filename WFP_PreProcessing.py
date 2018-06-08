import pandas as pd

df = pd.read_csv("WFPVAM_FoodPrices_05-12-2017.csv", encoding="ISO-8859-1")

# verandert de kolomnamen
df.columns = ["country_id", "country", "region_id", "region", "city_id", "city", "food_id", "food", "network_id", "network", "type_id", "type", "quantity", "unit_measure", "month", "year", "price", "commodity_source"]

# haalt de dollar tekens en hashtags uit de namen van regio's weg
# for region in df["region"]:
#     if "$" in region:
#         region = region.replace("$", " ")
#     elif "#" in region:
#         region = region.replace("#", " ")

print(df["region"].iloc[176614:176659])

df.loc[df.region_id == 0, "region"] = "Unknown"


# df = df.groupby(df["food"]).describe()

# df.to_csv("out.csv")

# print(df)
