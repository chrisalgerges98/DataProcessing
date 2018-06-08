import pandas as pd
import numpy as np

# import csv dataset
dataset = pd.read_csv("UNDataraw.csv")

# itereert over dataset en doet blablabla
for column in dataset:
    dataset2 = dataset["Total refugees"].groupby([dataset['Target country'], dataset['Year']]).sum()
    print(pd.to_numeric(dataset2, downcast='signed'))






#for x in range(len(dataset)):
#    if 


#for country in dataset["Country or territory of asylum or residence"]:
#   for year in dataset["Year"]: