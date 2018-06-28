import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import DataRange1d

# reads necessary data from csv
df = pd.read_csv("WFPFinal.csv")

# list of countries
countries = df["country"].unique()

# list of colors
my_palette = ['goldenrod', 'forestgreen', 'black', 'blue', 'blueviolet', 'brown','crimson', \
'darkblue', 'darkcyan', 'darkgreen', 'limegreen', 'darkkhaki', 'darkred', 'darkseagreen', 'darkviolet', 'deeppink', \
'green', 'indigo', 'magenta', 'maroon', 'navy', 'orange', 'orchid', 'purple', \
'red', 'sienna', 'teal', 'turquoise', 'violet', 'yellow']

# creates charts of multiple lines per country
# it displays the average price_per_unit over time
# the lines represent the price of a product
fOut = open("CountryChart.html", "a")
for country in countries:
    products = df["food"][df["country"] == country].unique()
    f = figure(plot_width=1000, plot_height=650, title=country)
    f.xaxis.axis_label="year"
    f.yaxis.axis_label="price per unit"
    for product, color in zip(products, my_palette):
        f.line(df["year"][(df["country"] == country) & (df["food"] == product)], \
        df["price_per_unit"][(df["country"] == country) & (df["food"] == product)], color=color, \
        alpha=0.8, muted_color=color, muted_alpha=0.2, legend=product)
    f.legend.spacing =
    html = file_html(f, CDN, "CountryChart")
    fOut.write(html)
fOut.close()
