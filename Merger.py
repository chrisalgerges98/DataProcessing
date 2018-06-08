import pandas as pd

result = pd.merge(pd.read_csv('YearlyRefugeeOutput.csv'), pd.read_csv('YearlyRefugeeInput.csv'), how='outer', on=('Country', 'Year'))
result = result.fillna(0)
print(result)
result.to_csv('YearlyRefugees.csv')