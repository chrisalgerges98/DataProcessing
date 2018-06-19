import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import DataRange1d

df = pd.read_csv("WFPFinal.csv")

countries = df["country"].unique()
# print(df["food"][df["country"] == "Ethiopia"])

# Afghan_fuel = df["year"][(df["country"] == "Afghanistan") & (df["food"] == "Fuel (diesel)")]
# Afghan_rice = df["year"][(df["country"] == "Afghanistan") & (df["food"] == "Rice (low quality)")]
# Afghan_wheat = df["year"][(df["country"] == "Afghanistan") & (df["food"] == "Wheat")]
#
# y_1 = df["average_price"][(df["country"] == "Afghanistan") & (df["food"] == "Fuel (diesel)")]
# y_2 = df["average_price"][(df["country"] == "Afghanistan") & (df["food"] == "Rice (low quality)")]
# y_3 = df["average_price"][(df["country"] == "Afghanistan") & (df["food"] == "Wheat")]
#
# output_file("Afghanistan.html")
#
# f = figure(plot_width=300, plot_height=300)
#
# f.multi_line(xs = [Afghan_fuel, Afghan_rice, Afghan_wheat], ys = [y_1, y_2, y_3], color=["red", "green", "blue"])
#
# show(f)

# f.multi_line(xs = [df["year"][(df["country"] == "Afghanistan") & (df["food"] == "Fuel (diesel)")],
#                    df["year"][(df["country"] == "Afghanistan") & (df["food"] == "Rice (low quality)")]
#                    df["year"][(df["country"] == "Afghanistan") & (df["food"] == "Wheat")]])

for country in countries:
    x_list = []
    y_list = []
    products = df["food"][df["country"] == country]
    for product in products:
        x = df["year"][(df["country"] == country) & (df["food"] == product)]
        # print(x)
        y = df["price_per_unit"][(df["country"] == country) & (df["food"] == product)]
        x_list.append(x)
        y_list.append(y)
    fOut = open("CountryChart.html", "a")
    f = figure(plot_width=500, plot_height=500, title=country)
    f.xaxis.axis_label="year"
    f.yaxis.axis_label="price per unit"
    f.multi_line(xs = x_list, ys = y_list)
    html = file_html(f, CDN, "chart1")
    fOut.write(html)
    fOut.close()
