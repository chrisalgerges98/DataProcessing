import pandas as pd

df = pd.read_csv("WFPVAM_FoodPrices_05-12-2017.csv", encoding="ISO-8859-1")

# changes column names
df.columns = ["country_id", "country", "region_id", "region", "city_id", "city", "food_id", "food", "currency_id", "currency", "market_id", "market", "unit_id", "unit_measure", "month", "year", "price", "commodity_source"]

# drops irrelevant data from the dataset
df = df.drop(df[(df.year < 2001) | (df.year > 2016)].index)
df = df.drop(df[df.food == "Exchange rate"].index)
df = df.drop(df[df.food == "Exchange rate (unofficial)"].index)
df = df.drop(df[df.food == "Wage (non-qualified labour)"].index)
df = df.drop(df[df.food == "Wage (non-qualified labour, agricultural)"].index)
df = df.drop(df[df.food == "Wage (non-qualified labour, non-agricultural)"].index)
df = df.drop(df[df.food == "Wage (qualified labour)"].index)
df = df.drop(df[df.food == "Transport (public)"].index)
df = df.drop(df[(df.country == "Somalia") | (df.country == "Timor-Leste")].index)

# calculates the average price per country, per product, per year
df = df["price"].groupby([df["country"], df["food"], df["currency"], df["year"], df["unit_measure"]]).mean().round(decimals=2)

# groups by unit id and unit measure
df = df.groupby([df["unit_id"], df["unit_measure"]]).mean()

# writes data to a csv file
df.to_csv("WFPAveragePrice.csv", header=["average_price"])

# counts the number of years where there is data from a product
def counter():
    df = pd.read_csv("WFPAveragePrice.csv")
    df = df["year"].groupby([df["country"], df["food"]]).count()
    df.to_csv("WFPYearlyCount.csv", header=["count"])

# drops the rows where the count is less than 5
# (so the price of a product has to be recorded at least five years)
def drop():
    df = pd.read_csv("WFPYearlyCount.csv")
    df.count = df["count"].astype("int64")
    df = df.drop(df[df.count < 5].index)
    df.to_csv("WFPYearlyCountCleaned.csv")

# merges two dataframes
def merge():
    df = pd.merge(pd.read_csv("WFPAveragePrice.csv"), pd.read_csv("WFPYearlyCountCleaned.csv"), how="inner", on=("country", "food"))

    df.to_csv("WFPCleaned.csv")

# function calls
counter()
drop()
merge()
