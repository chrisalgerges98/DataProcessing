import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

land =['MijnlandAfrica']

regio =["MijnlandAfrica","Benin","Burkina Faso","Burundi","Cameroon","Central African Republic","Chad","Congo","Democratic Republic of the Congo","Cote d'Ivoire","Djibouti","Egypt","Ethiopia","Gambia","Ghana","Guinea","Guinea-Bissau","Kenya","Lesotho","Liberia","Madagascar","Malawi","Mali","Mauritania","Mozambique","Niger","Nigeria","Rwanda","Senegal","South Sudan","Sudan","Swaziland",'Uganda','United Republic of Tanzania','Yemen','Zambia','Zimbabwe']



df = pd.read_csv("WFPFinal.csv")

countries = df["country"].unique()

# change to get charts about regions and certain product
product = "Maize"
for i, country in zip(range(len(land)), countries):
    x_list = []
    y_list = []
    if product in df["food"][(df["country"] == country)].unique():
        #print(land[i])
        for j in regio[i]:
            x = df["year"][(df["country"] == j) & (df["food"] == product)]
            #print(x)
            y = df["price_per_unit"][(df["country"] == j) & (df["food"] == product)]
            x_list.append(x)
            y_list.append(y)
        fOut = open("Afrika_ppChart.html", "a")
        f = figure(plot_width=500, plot_height=500, title=country)
        f.multi_line(xs = x_list, ys = y_list)
        html = file_html(f, CDN, "chart")
        fOut.write(html)
        fOut.close()
    else:
        continue
