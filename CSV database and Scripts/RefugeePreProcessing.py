# De functies in dit programma werken los van elkaar, en niet als één geheel. Handmatige aanpassing op de csv's tussendoor is vereist.

import pandas as pd
import numpy as np

# import refugee csv dataset
UNRaw = pd.read_csv("UNDataraw.csv")

# gets the total amount of refugees output per country per year
def yearlyOrigin(dataset):
    dataset2 = pd.to_numeric(dataset["Total refugees"].groupby([dataset['Origin country'], dataset['Year']]).sum(), downcast='signed')
    dataset2.columns = "Country, Year, Total refugees"
    dataset2.to_csv("YearlyRefugeeOutput.csv", header="Country, Year, Total refugees out")
    return dataset2

# gets the mount of refugees input per country per year
def yearlyTarget(dataset):
    dataset2 = pd.to_numeric(dataset["Total refugees"].groupby([dataset['Target country'], dataset['Year']]).sum(), downcast='signed')
    dataset2.to_csv("YearlyRefugeeInput.csv", header='Country, Year, Total refugees in')
    return dataset2

# merge input en output in a new csv
def merger():
    result = pd.merge(pd.read_csv('YearlyRefugeeOutput.csv'), pd.read_csv('YearlyRefugeeInput.csv'), how='outer', on=('Country', 'Year'))
    result = result.fillna(0)
    result['Total refugees in'] = result['Total refugees in'].apply(np.int64)
    result['Total refugees out'] = result['Total refugees out'].apply(np.int64)
    #print(result)
    result.to_csv('YearlyRefugees.csv')

# sorts per country and then per year
def sorter():
    data = pd.read_csv("YearlyRefugees.csv")
    data = data.sort_values(['Country', 'Year'])
    data.to_csv('YearlyRefugees.csv')


# below the function callers
yearlyTarget(UNRaw)
yearlyOrigin(UNRaw)
merger()
sorter()
