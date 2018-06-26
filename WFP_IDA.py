import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import DataRange1d, Legend, ColumnDataSource
from bokeh.models import PanTool, ResetTool, WheelZoomTool, HoverTool, LassoSelectTool, BoxSelectTool

df = pd.read_csv("WFPAfricaFinal.csv")
countries = ["Senegal", "Uganda"]
products = ["Maize (imported)", "Millet", "Sorghum", "Maize (white)"]

my_palette = ['goldenrod', 'forestgreen', 'black', 'blue', 'blueviolet', 'brown','crimson',
'darkblue', 'darkcyan', 'darkgreen', 'limegreen', 'darkkhaki', 'darkred', 'darkseagreen', 'darkviolet', 'deeppink',
'green', 'indigo', 'magenta', 'maroon', 'navy', 'orange', 'orchid', 'purple',
'red', 'sienna', 'teal', 'turquoise', 'violet', 'yellow']

fOut = open("SenegalAndUgandaChart.html", "a")
for country in countries:
    f = figure(plot_width=1000, plot_height=650, title=country)
    legend_it = []
    for product, color in zip(products, my_palette):
        source = ColumnDataSource(name = "data", data=dict(
            year = df["year"][(df["country"] == country) & (df["food"] == product)],
            price_per_unit = df["price_per_unit"][(df["country"] == country) & (df["food"] == product)]
        ))
        hover = HoverTool(tooltips=[
            ("year", "@year"),
            ("price_per_unit", "@price_per_unit")
        ], mode='vline')
        c = f.line(x='year', y='price_per_unit', line_width=2, color=color, legend=source.name, alpha=0.8, source=source)
        legend_it.append((product, [c]))
    f.toolbar.tools = [PanTool(), ResetTool(), WheelZoomTool(), hover, LassoSelectTool(), BoxSelectTool()]
    legend = Legend(items=legend_it, location=(0, 10))
    f.xaxis.axis_label="year"
    f.yaxis.axis_label="price per unit"
    legend.click_policy="hide"
    f.legend.visible=False
    f.add_layout(legend, "right")
    html = file_html(f, CDN, "SenegalAndUgandaChart")
    fOut.write(html)
fOut.close()

# df_2 = pd.read_csv("CorrData.csv")
# s1 = df_2["Benin_Maize"]
# s2 = df_2["Benin_Millet"]
# correlation = s1.corr(s2).round(decimals=2)
# print(correlation)

# df_3 = pd.read_csv("AverageCountry.csv")

# fOut = open("BeninAverageChart.html", "a")
# f = figure(plot_width=750, plot_height=350, title="average price per country of Maize, Sorghum and Millet")
# legend_it = []
# for country, color in zip(countries, my_palette):
#     source = ColumnDataSource(name = "data", data=dict(
#         average_price = df_3["price"][df_3["country"] == country],
#         year= df_3["year"][df_3["country"] == country]
#     ))
#     hover = HoverTool(tooltips=[
#         ("year", "@year"),
#         ("average_price", "@average_price")
#     ], mode="vline")
#     c = f.line(x="year", y="average_price", line_width=2, color=color, legend=source.name, alpha=0.8, muted_color=color, muted_alpha=0.1, source=source)
#     legend_it.append((country, [c]))
# f.toolbar.tools = [PanTool(), ResetTool(), WheelZoomTool(), hover, LassoSelectTool(), BoxSelectTool()]
# f.xaxis.axis_label = "year"
# f.yaxis.axis_label = "average_price"
# legend = Legend(items=legend_it, location=(0,-10))
# legend.click_policy="hide"
# f.legend.visible=False
# f.add_layout(legend, "right")
# html = file_html(f, CDN, "BeninAverageChart")
# fOut.write(html)
# fOut.close()
