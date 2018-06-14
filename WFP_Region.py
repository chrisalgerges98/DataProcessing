import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

land = ['Benin']
regio = [['Benin', 'Burkina Faso', 'Nigeria', 'Niger']]

df = pd.read_csv("WFPCleaned.csv")
#dataset = pd.read_csv("Regions.csv", delimiter=':')

countries = df["country"].unique()
#regions = dataset["neighbours"]
#print(regions)

#for country in countries:
#fill in country for country
#country = "Benin"
#countries = dataset["neighbours"][dataset["country"] == country]
#print(countries)
x_list = []
y_list = []

    #products = df["food"][df["country"] == country].unique()
    #fill in product for product
product = "Maize"
#years = df["year"][df["country"] == country].unique()
     #for product in products:
     #for year in years:
# x = df["year"][(df["country"] == country) & (df["food"] == product)]
# print(x)
# y = df["average_price"][(df["country"] == country) & (df["food"] == product)]
# x_list.append(x)
# y_list.append(y)
for i in range(len(land)):
    print(land[i])
    for j in regio[i]:
        x = df["year"][(df["country"] == j) & (df["food"] == product)]
        print(x)
        y = df["average_price"][(df["country"] == j) & (df["food"] == product)]
        x_list.append(x)
        y_list.append(y)
fOut = open("benin.html", "a")
f = figure(plot_width=500, plot_height=500, title=country)
f.multi_line(xs = x_list, ys = y_list)
html = file_html(f, CDN, "chart1")
fOut.write(html)
fOut.close()
