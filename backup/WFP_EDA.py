import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import DataRange1d, Legend

df = pd.read_csv("WFPAfricaFinal.csv")

countries = df["country"].unique()
my_palette = ['goldenrod', 'forestgreen', 'black', 'blue', 'blueviolet', 'brown','crimson', \
'darkblue', 'darkcyan', 'darkgreen', 'limegreen', 'darkkhaki', 'darkred', 'darkseagreen', 'darkviolet', 'deeppink', \
'green', 'indigo', 'magenta', 'maroon', 'navy', 'orange', 'orchid', 'purple', \
'red', 'sienna', 'teal', 'turquoise', 'violet', 'yellow']
# print(df["food"][df["country"] == "Ethiopia"])

fOut = open("CountryChart.html", "a")
for country in countries:
    legend_it = []
    products = df["food"][df["country"] == country].unique()
    f = figure(plot_width=1000, plot_height=650, title=country)
    f.xaxis.axis_label="year"
    f.yaxis.axis_label="price per unit"
    for product, color in zip(products, my_palette):
        c = f.line(df["year"][(df["country"] == country) & (df["food"] == product)], \
        df["price_per_unit"][(df["country"] == country) & (df["food"] == product)], color=color, \
        alpha=0.8, muted_color=color, muted_alpha=0.2)
        legend_it.append((product, [c]))
    legend = Legend(items=legend_it, location=(0, -20))
    legend.click_policy="mute"
    f.add_layout(legend, "right")
    html = file_html(f, CDN, "CountryChart")
    fOut.write(html)
fOut.close()



# import pandas as pd
# from bokeh.palettes import Spectral4
# from bokeh.plotting import figure, output_file, show
# from bokeh.sampledata.stocks import AAPL, IBM, MSFT, GOOG
# from bokeh.models import Legend
#
# p = figure(plot_width=800, plot_height=250, x_axis_type="datetime", toolbar_location='above')
# p.title.text = 'Click on legend entries to mute the corresponding lines'
#
# legend_it = []
#
# for data, name, color in zip([AAPL, IBM, MSFT, GOOG], ["AAPL", "IBM", "MSFT", "GOOG"], Spectral4):
#     df = pd.DataFrame(data)
#     df['date'] = pd.to_datetime(df['date'])
#     c = p.line(df['date'], df['close'], line_width=2, color=color, alpha=0.8,
#            muted_color=color, muted_alpha=0.2)
#     legend_it.append((name, [c]))
#
#
# legend = Legend(items=legend_it, location=(0, -60))
# legend.click_policy="mute"
#
# p.add_layout(legend, 'right')
# print(c)
# show(p)
