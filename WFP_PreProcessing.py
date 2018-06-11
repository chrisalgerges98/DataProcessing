import pandas as pd

df = pd.read_csv("WFPVAM_FoodPrices_05-12-2017.csv", encoding="ISO-8859-1")

# verandert de kolomnamen
df.columns = ["country_id", "country", "region_id", "region", "city_id", "city", "food_id", "food", "currency_id", "currency", "market_id", "market", "unit_id", "unit_measure", "month", "year", "price", "commodity_source"]

# df = df.groupby([df["unit_id"], df["unit_measure"]]).mean()

# dropt irrelevante data
df = df.drop(df[(df.year < 2001) | (df.year > 2016)].index)
df = df.drop(df[df.food == "Exchange rate"].index)
df = df.drop(df[df.food == "Exchange rate (unofficial)"].index)
df = df.drop(df[df.food == "Wage (non-qualified labour)"].index)
df = df.drop(df[df.food == "Wage (non-qualified labour, agricultural)"].index)
df = df.drop(df[df.food == "Wage (non-qualified labour, non-agricultural)"].index)
df = df.drop(df[df.food == "Wage (qualified labour)"].index)
df = df.drop(df[df.food == "Transport (public)"].index)

# berekent de gemiddelde prijs in twee decimalen per land, per voedingsmiddel, per jaar
df = df["price"].groupby([df["country"], df["food"], df["year"]]).mean().round(decimals=2)

# stopt het in een csv file
df.to_csv("WFPAveragePrice.csv", header="average_price")

def counter():
    df = pd.read_csv("WFPAveragePrice.csv")
    df = df["year"].groupby([df["country"], df["food"]]).count()
    df.to_csv("WFPYearlyCount.csv", header="count")

def drop():
    df = pd.read_csv("WFPYearlyCount.csv")
    df.year = df["year"].astype("int64")
    df = df.drop(df[df.year < 5].index)
    df.to_csv("WFPYearlyCountCleaned.csv")

def merge():
    df = pd.merge(pd.read_csv("WFPAveragePrice.csv"), pd.read_csv("WFPYearlyCountCleaned.csv"), how="inner", on=("country", "food"))
    df.to_csv("WFPAveragePriceCleaned")

counter()
drop()
merge()
