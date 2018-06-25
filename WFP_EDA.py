import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.io import output_file
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import DataRange1d, Legend, ColumnDataSource
from bokeh.models import PanTool, ResetTool, WheelZoomTool, HoverTool, LassoSelectTool, BoxSelectTool
import sklearn
from sklearn.linear_model import LinearRegression


df = pd.read_csv("WFPAfricaFinal.csv")
df_2 = pd.read_csv("Ref_vs_Pop.csv")

countries = df_2["Country"].unique()
my_palette = ['goldenrod', 'forestgreen', 'black', 'blue', 'blueviolet', 'brown','crimson', \
'darkblue', 'darkcyan', 'darkgreen', 'limegreen', 'darkkhaki', 'darkred', 'darkseagreen', 'darkviolet', 'deeppink', \
'green', 'indigo', 'magenta', 'maroon', 'navy', 'orange', 'orchid', 'purple', \
'red', 'sienna', 'teal', 'turquoise', 'violet', 'yellow']


# # creates per country a multiline plot
# # which displays the price of products over time
# fOut = open("CountryChart.html", "a")
# for country in countries:
#     legend_it = []
#     products = df["food"][df["country"] == country].unique()
#     f = figure(plot_width=1000, plot_height=650, title=country)
#     for product, color in zip(products, my_palette):
#         source = ColumnDataSource(name = 'data', data=dict(
#             year = df["year"][(df["country"] == country) & (df["food"] == product)],
#             price_per_unit = df["price_per_unit"][(df["country"] == country) & (df["food"] == product)]
#         ))
#         hover = HoverTool(tooltips=[
#             ("year", "@year"),
#             ("price_per_unit", "@price_per_unit")
#         ], mode='vline')
#         c = f.line(x='year', y='price_per_unit', line_width=2, color=color, legend=source.name, alpha=0.8, muted_color=color, muted_alpha=0.1, source=source)
#         legend_it.append((product, [c]))
#     f.toolbar.tools = [PanTool(), ResetTool(), WheelZoomTool(), hover, LassoSelectTool(), BoxSelectTool()]
#     f.xaxis.axis_label="year"
#     f.yaxis.axis_label="price per unit"
#     legend = Legend(items=legend_it, location=(0, 10))
#     legend.click_policy="hide"
#     f.legend.visible = False
#     f.add_layout(legend, "right")
#     html = file_html(f, CDN, "CountryChart")
#     fOut.write(html)
# fOut.close()


# creates scatterplots between the rate of change of the number of refugees
# in percentage of the population of the country
# and the rate of change of the average price per country
fOut = open("ScatterplotPrice_vs_Refugee.html", "a")
for country in countries:
    f = figure(plot_width=550, plot_height=350, title=country)
    source = ColumnDataSource(data=dict(
        RefugeePercentagePopulation = df_2["Percent_ref_vs_pop"][df_2["Country"] == country],
        RateOfChangePrice = df_2["Rate_of_change_price"][df_2["Country"] == country]
    ))
    f.xaxis.axis_label="refugees vs population"
    f.yaxis.axis_label="rate of change price"
    hover = HoverTool(tooltips=[
        ("refugees vs population", "@RefugeePercentagePopulation"),
        ("rate of change price", "@RateOfChangePrice")
    ])
    f.toolbar.tools = [PanTool(), ResetTool(), WheelZoomTool(), hover, LassoSelectTool(), BoxSelectTool()]
    f.circle(x='RefugeePercentagePopulation', y='RateOfChangePrice', size=12, source=source)
    html = file_html(f, CDN, "ScatterplotPrice_vs_Refugee")
    fOut.write(html)
fOut.close()

X = df_2["Percent_ref_vs_pop"][df["country"] == "Burundi"]
Y = df_2["Rate_of_change_price"][df["country"] == "Burundi"]
