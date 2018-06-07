import pandas as pd

df = pd.read_csv("WFPVAM_FoodPrices_05-12-2017.csv", encoding="ISO-8859-1")

df.columns = ["country_id", "country", "region_id", "region", "city_id", "city", "food_id", "food", "network_id", "network", "type_id", "type", "quantity", "unit_measure", "month", "year", "price", "commodity_source"]

print(df)
