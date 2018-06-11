import pandas as pd
import numpy as np

# import csv dataset
UNRaw = pd.read_csv("UNDataraw.csv")

# haalt totale jaarlijkse refugees output per land uit dataset 
def yearlyOrigin(dataset):
    dataset2 = pd.to_numeric(dataset["Total refugees"].groupby([dataset['Origin country'], dataset['Year']]).sum(), downcast='signed')
    dataset2.columns = ["Country", "Year", "Total refugees"]
    dataset2.to_csv("YearlyRefugeeOutput.csv", header='Country, Year, Total refugees out')
    return dataset2

# haalt jaarlijkse refugees input per land uit dataset
def yearlyTarget(dataset):
    dataset2 = pd.to_numeric(dataset["Total refugees"].groupby([dataset['Target country'], dataset['Year']]).sum(), downcast='signed')
    dataset2.to_csv("YearlyRefugeeInput.csv", header='Country, Year, Total refugees in')
    return dataset2

# merged beide totale refugee csv's
def merger(): 
    result = pd.merge(pd.read_csv('YearlyRefugeeOutput.csv'), pd.read_csv('YearlyRefugeeInput.csv'), how='outer', on=('Country', 'Year'))
    result = result.fillna(0)
    result = result.sort_values('Country')
    result['Total refugees in'] = result['Total refugees in'].apply(np.int64)
    result['Total refugees out'] = result['Total refugees out'].apply(np.int64)
    print(result)
    result.to_csv('YearlyRefugees.csv')

def sorter():
    data = pd.read_csv("YearlyRefugees.csv")
    data = data.sort_values(['Country', 'Year'])
    data.to_csv('YearlyRefugees.csv')

sorter()

#yearlyTarget(UNRaw)
#yearlyOrigin(UNRaw)
#merger()




# VANAF HIER RANDOM BULLSHIT:

#dataset2.to_csv("YearlyRefugeeOutput.csv")
#dataset3 = pd.to_numeric(dataset["Total refugees"].groupby([dataset['Target country'], dataset['Year']]).sum(), downcast='signed')

#print(pd.to_numeric(dataset["Target Country"].groupby([dataset['Origin country'], dataset['Year']]).sum(), downcast='signed'))

#print(pd.to_numeric(dataset2, downcast='signed'))