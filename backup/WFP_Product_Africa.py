import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.models import Legend

#list of countries on the continent Africa
land =[["Benin"],
["Burkina Faso"],
["Burundi"],
["Cameroon"],
["Central African Republic"],
["Chad"],
["Congo"],
["Democratic Republic of the Congo"],
["Ivory Coast"],
["Djibouti"],
["Egypt"],
["Ethiopia"],
["Gambia"],
["Ghana"],
["Guinea"],
["Guinea-Bissau"],
["Kenya"],  
["Lesotho"],
["Liberia"],
["Madagascar"],
["Malawi"],
["Mali"],
["Mauritania"],
["Mozambique"],
["Niger"],
["Nigeria"],
["Rwanda"],
["Senegal"],
["South Sudan"],
["Sudan"],
["Swaziland"],
["Uganda"],
["United Republic of Tanzania"],
["Zambia"],
["Zimbabwe"],
["MijnlandAfrica"]]

#list of region(country+neigbouring countries) on the continent Africa
regio =[["Benin","Burkina Faso", "Nigeria", "Niger"],
["Burkina Faso","Mali", "Ivory Coast", "Ghana", "Benin", "Niger"],
["Burundi","Democratic Republic of the Congo", "Rwanda", "United Republic of Tanzania"],
["Cameroon","Nigeria", "Chad", "Central African Republic", "Congo"],
["Central African Republic", "Congo", "Democratic Republic of the Congo", "Chad", "Sudan", "South Sudan"],
["Chad","Niger", "Nigeria", "Sudan", "Central African Republic", "Cameroon"],
["Congo","Democratic Republic of the Congo", "Cameroon", "Central African Republic"],
["Democratic Republic of the Congo","Congo", "Zambia", "Rwanda", "Burundi", "United Republic of Tanzania", "Uganda", "South Sudan", "Central African Republic"],
["Ivory Coast", "Guinea", "Liberia", "Ghana", "Mali", "Burkina Faso"],
["Djibouti","Ethiopia","Yemen"],
["Egypt","Sudan"],
["Ethiopia","Sudan", "Djibouti", "South Sudan", "Kenya"],
["Gambia","Senegal"],
["Ghana","Ivory Coast", "Burkina Faso"],
["Guinea","Ivory Coast", "Liberia", "Guinea-Bissau", "Senegal", "Mali"],
["Guinea-Bissau","Guinea", "Senegal"],
["Kenya", "Ethiopia", "Uganda", "United Republic of Tanzania"],
["Lesotho"],
["Liberia","Guinea", "Ivory Coast"],
["Madagascar"],
["Malawi","Mozambique", "Zambia", "United Republic of Tanzania"],
["Mali","Niger", "Burkina Faso", "Ivory Coast", "Mauritania", "Senegal", "Guinea"],
["Mauritania","Mali", "Senegal"],
["Mozambique","Malawi", "United Republic of Tanzania", "Zambia", "Swaziland", "Zimbabwe"],
["Niger","Mali", "Chad", "Nigeria", "Benin", "Burkina Faso"],
["Nigeria","Cameroon", "Chad", "Niger", "Benin"],
["Rwanda","Uganda", "United Republic of Tanzania", "Burundi", "Democratic Republic of the Congo"],
["Senegal","Gambia", "Guinea", "Guinea-Bissau", "Mali", "Mauritania"],
["South Sudan","Ethiopia", "Kenya", "Uganda", "Democratic Republic of the Congo", "Central African Republic"],
["Sudan","Chad", "Central African Republic", "Egypt", "Ethiopia"],
["Swaziland","Mozambique"],
["Uganda","Kenya", "South Sudan", "Democratic Republic of the Congo", "Rwanda", "United Republic of Tanzania"],
["United Republic of Tanzania","Kenya", "Uganda", "Rwanda", "Burundi", "Democratic Republic of the Congo", "Zambia", "Malawi"],
["Zambia","United Republic of Tanzania", "Malawi", "Mozambique", "Zimbabwe"],
["Zimbabwe", "Zambia", "Mozambique"],
["MijnlandAfrica","Benin","Burkina Faso","Burundi","Cameroon","Central African Republic","Chad","Congo","Democratic Republic of the Congo","Ivory Coast","Djibouti","Egypt","Ethiopia","Gambia","Ghana","Guinea","Guinea-Bissau","Kenya","Lesotho","Liberia","Madagascar","Malawi","Mali","Mauritania","Mozambique","Niger","Nigeria","Rwanda","Senegal","South Sudan","Sudan","Swaziland",'Uganda','United Republic of Tanzania','Yemen','Zambia','Zimbabwe',]]

# Colours for graph lines
my_palette = ['goldenrod', 'forestgreen', 'black', 'blue', 'blueviolet', 'brown','crimson', \
'darkblue', 'darkcyan', 'darkgreen', 'limegreen', 'darkkhaki', 'darkred', 'darkseagreen', 'darkviolet', 'deeppink', \
'green', 'indigo', 'magenta', 'maroon', 'navy', 'orange', 'orchid', 'purple', \
'red', 'sienna', 'teal', 'turquoise', 'violet', 'yellow']
# print(df["food"][df["country"] == "Ethiopia"])

df = pd.read_csv("WFPAfricaFinal.csv")
df2 = pd.read_csv("ProductsInAfrica.csv")

products = df2["food"].unique()

x_list = []
y_list = []

fOut = open("ProductChart.html", "a")
for product in products:
    legend_it = []
    countries = df["country"][df["food"] == product].unique()
    f = figure(plot_width=1000, plot_height=650, title=product)
    f.xaxis.axis_label="Year"
    f.yaxis.axis_label="Price per unit"
    for country, color in zip(countries, my_palette):
        c = f.line(df["year"][(df["country"] == country) & (df["food"] == product)], \
        df["price_per_unit"][(df["country"] == country) & (df["food"] == product)], color=color, \
        alpha=0.8, muted_color=color, muted_alpha=0.2, line_width=3)
        legend_it.append((country, [c]))
    legend = Legend(items=legend_it, location=(0, -20))
    legend.click_policy="mute"
    f.add_layout(legend, "right")
    html = file_html(f, CDN, "ProductChart")
    fOut.write(html)
fOut.close()