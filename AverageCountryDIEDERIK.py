import pandas as pd
import numpy as np 

columns = ["price_benin", "price_burkina_faso", "price_mali", "price_niger"]

df = pd.read_csv("AverageCountryDIEDERIK.csv")

# fd = open("derkaderka.csv", "a")

for column in columns:
    for column1 in columns:
        result = df[column1].corr(df[column])
        print(result)
    
        


# fd.close