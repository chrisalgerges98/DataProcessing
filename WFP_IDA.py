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

df = pd.read_csv("WFPAfricaFinal.csv")
countries = df["country"].unique()
years = sorted(df["year"].unique())

def chunks(l, n):
    new_list = []
    for i in range(0, len(l), n):
        elem = l[i:i+n]
        new_list.append(elem)
    return new_list

def price_per_year(country, foodtype):
    prices = []
    for year in years:
        for food in foodtype:
            df_1 = df["price_per_unit"][(df["food"] == food) & (df["year"] == year) & (df["country"] == country)]
            prices.append(df_1)
    new_list = chunks(prices, len(foodtype))

    new_list_2 = []
    for i in new_list:
        i = [x for x in i if not(x.empty)]
        new_list_2.append(i)

    price_per_year = []
    new_list_2 = [z for z in new_list_2 if z != []]

    for k in new_list_2:
        k = [elem.mean() for elem in k]
        average_price = sum(k) / len(k)
        price_per_year.append(average_price)
    return price_per_year

# for foodtype in Alle_producten:
#
