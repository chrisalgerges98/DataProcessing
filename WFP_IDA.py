import pandas as pd
import numpy as np
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import DataRange1d, Legend, ColumnDataSource
from bokeh.models import PanTool, ResetTool, WheelZoomTool, HoverTool, LassoSelectTool, BoxSelectTool

Alle_soorten_eetbare_Olien = ["Oil (palm)", "Oil (vegetable)" ,"Oil (vegetable imported)",
"Oil (sunflower)", "Oil (vegetable local)"]

Alle_soorten_vlees = ["Meat (beef)", "Meat (chicken frozen)", "Meat (chicken)", "Meat (goat with bones)", "Meat (goat)"]

Alle_soorten_vis = ["Fish (smoked)", "Fish (fresh)", "Fish (salted)", "Fish (appolo)", "Fish (dry)"]

Alle_soorten_vlees_en_vis = ["Meat (beef)", "Meat (chicken frozen)", "Meat (chicken)", "Meat (goat with bones)", "Meat (goat)",
"Fish (smoked)", "Fish (fresh)", "Fish (salted)", "Fish (appolo)", "Fish (dry)"]

Alle_graanproducten = ["Maize", "Maize (white)", "Millet", "Sorghum", "Sorghum (red)", "Sorghum (white)", "Maize (flour)",
"Maize meal", "Bread", "Pasta", "Oil (maize)", "Wheat", "Maize (local)", "Fonio", "Cornstarch", "Bread (brown)",
"Sorghum (taghalit)", "Maize meal (white first grade)", "Maize meal (white with bran)", "Wheat flour (local)", "Sorghum flour",
"Maize (imported)", "Millet (white)", "Sorghum (food aid)", "Maize meal (white breakfast)", "Maize meal (white roller)"]

Alle_rijst_producten = ["Rice (imported)", "Rice (local)", "Rice", "Rice (mixed low quality)", "Rice (long grain imported)",
"Rice (medium grain imported)", "Rice (paddy long grain local)", "Rice (small grain imported)", "Rice (denikassia imported)",
"Rice (white imported)", "Rice (paddy)", "Rice (imported Tanzanian)"]

Alle_producten = [Alle_soorten_eetbare_Olien, Alle_soorten_vlees, Alle_soorten_vis, Alle_soorten_vlees_en_vis, Alle_graanproducten, Alle_rijst_producten]
Titles = ["Alle_soorten_eetbare_Olien", "Alle_soorten_vlees", "Alle_soorten_vis", "Alle_soorten_vlees_en_vis", "Alle_graanproducten", "Alle_rijst_producten"]


df = pd.read_csv("WFPAfricaFinal.csv")
years = sorted(df["year"].unique())
countries = ["Burkina Faso", "Benin", "Nigeria", "Niger", "Mali"]
products = ["Maize", "Millet", "Sorghum"]

my_palette = ['goldenrod', 'forestgreen', 'black', 'blue', 'blueviolet', 'brown','crimson',
'darkblue', 'darkcyan', 'darkgreen', 'limegreen', 'darkkhaki', 'darkred', 'darkseagreen', 'darkviolet', 'deeppink',
'green', 'indigo', 'magenta', 'maroon', 'navy', 'orange', 'orchid', 'purple',
'red', 'sienna', 'teal', 'turquoise', 'violet', 'yellow']

# fOut = open("ChartSpecific.html", "a")
# f = figure(plot_width=1000, plot_height=650, title="average chart")
# for country in countries:
#     for product, color in zip(products, my_palette):
#         source = ColumnDataSource(data=dict(
#             year = df["year"][(df["country"] == country) & (df["food"] == product)],
#             price_per_unit = df["price_per_unit"][(df["country"] == country) & (df["food"] == product)]
#         ))
#         hover = HoverTool(tooltips=[
#             ("year", "@year"),
#             ("price_per_unit", "@price_per_unit")
#         ], mode='vline')
#         c = f.line(x='year', y='price_per_unit', line_width=2, color=color, legend=country, alpha=0.8, muted_color=color, muted_alpha=0.1, source=source)
#     f.toolbar.tools = [PanTool(), ResetTool(), WheelZoomTool(), hover, LassoSelectTool(), BoxSelectTool()]
#     f.xaxis.axis_label="year"
#     f.yaxis.axis_label="price per unit"
#     f.legend.click_policy="hide"
#     html = file_html(f, CDN, "CountryChartSpecific")
#     fOut.write(html)
# fOut.close()

# with open('my_csv.csv', 'a') as f:
#     for country in countries:
#         for food in products:
#             df_2 = df[(df["country"] == country) & (df["food"] == food)]
#             df_2.to_csv(f)

# def chunks(l, n):
#     new_list = []
#     for i in range(0, len(l), n):
#         elem = l[i:i+n]
#         new_list.append(elem)
#     return new_list
#
# def price_per_year(country):
#     prices = []
#     for year in years:
#         df_1 = df["price_per_unit"][(df["year"] == year) & (df["country"] == country)]
#         prices.append(df_1)
#     new_list = chunks(prices, len(products))
#
#     new_list_2 = []
#     for i in new_list:
#         i = [x for x in i if not(x.empty)]
#         new_list_2.append(i)
#
#     price_per_year = []
#     new_list_2 = [z for z in new_list_2 if z != []]
#
#     for k in new_list_2:
#         k = [elem.mean() for elem in k]
#         average_price = sum(k) / len(k)
#         price_per_year.append(average_price)
#     return price_per_year


df_3 = pd.read_csv("AverageCountry.csv")

fOut = open("BeninAverageChart.html", "a")
f = figure(plot_width=750, plot_height=350, title="average price per country of Maize, Sorghum and Millet")
legend_it = []
for country, color in zip(countries, my_palette):
    source = ColumnDataSource(name = "data", data=dict(
        average_price = df_3["price"][df_3["country"] == country],
        year= df_3["year"][df_3["country"] == country]
    ))
    hover = HoverTool(tooltips=[
        ("year", "@year"),
        ("average_price", "@average_price")
    ], mode="vline")
    c = f.line(x="year", y="average_price", line_width=2, color=color, legend=source.name, alpha=0.8, muted_color=color, muted_alpha=0.1, source=source)
    legend_it.append((country, [c]))
f.toolbar.tools = [PanTool(), ResetTool(), WheelZoomTool(), hover, LassoSelectTool(), BoxSelectTool()]
f.xaxis.axis_label = "year"
f.yaxis.axis_label = "average_price"
legend = Legend(items=legend_it, location=(0,-10))
legend.click_policy="hide"
f.legend.visible=False
f.add_layout(legend, "right")
html = file_html(f, CDN, "BeninAverageChart")
fOut.write(html)
fOut.close()




# fOut = open("ChartSpecificAveragedChart.html", "a")
# f = figure(plot_width=550, plot_height=350, title="average price per country of Maize, Sorghum and Millet")
# for country in countries:
#     for food, color in zip(products, my_palette):
#         f.line(df_5["year"][(df_5["country"] == country) & (df_5["food"] == food)], df_5["price_per_unit"][(df["country"] == country) & (df_5["food"] == food)],
#         color=color, alpha=0.8, legend=country, muted_color=color, muted_alpha=0.1)
# f.xaxis.axis_label = "year"
# f.yaxis.axis_label = "average_price"
# f.legend.click_policy="hide"
# html = file_html(f, CDN, "ChartSpecificAveragedChart")
# fOut.write(html)
# fOut.close()


# fOut = open("FoodTypeChart.html", "a")
# for foodtype, title in zip(Alle_producten, Titles):
#     legend_it = []
#     f = figure(plot_width=1000, plot_height=650, title=title)
#     for country, color in zip(countries, my_palette):
#         source = ColumnDataSource(name = "data", data=dict(
#             price_per_year = price_per_year(country, foodtype),
#             year = years
#         ))
#         hover = HoverTool(tooltips=[
#             ("year", "@year"),
#             ("average_price", "@price_per_year")
#         ], mode ='vline')
#         c = f.line(x='year', y='price_per_year', line_width=2, color=color, legend=source.name, alpha=0.8, muted_color=color, muted_alpha=0.1, source=source)
#         if price_per_year != []:
#             legend_it.append((country, [c]))
#     f.toolbar.tools = [PanTool(), ResetTool(), WheelZoomTool(), hover, LassoSelectTool(), BoxSelectTool()]
#     f.xaxis.axis_label = "year"
#     f.yaxis.axis_label = "average_price"
#     legend = Legend(items=legend_it, location=(0, 0))
#     legend.click_policy="hide"
#     legend.spacing=1
#     f.legend.visible = False
#     f.add_layout(legend, "right")
#     html = file_html(f, CDN, "FoodTypeChart")
#     fOut.write(html)
# fOut.close()
