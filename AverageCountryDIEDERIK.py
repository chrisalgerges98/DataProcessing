import pandas as pd
import numpy as np 

columns = ["price_benin", "price_burkina_faso", "price_mali", "price_niger", "price_nigeria"]

df = pd.read_csv("AverageCountryDIEDERIK.csv")

# fd = open("derkaderka.csv", "a")

for column in columns:
    for column1 in columns:
        result = df.groupby('year')[column,column1].corr()
        with open("derkaderka.csv", "a") as f:
            result.to_csv(f, header=False)
        


# fd.close