import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

land =[["Benin"],
["Burkina Faso"],
["Burundi"],
["Cameroon"],
["Central African Republic"],
["Chad"],
["Congo"],
["Democratic Republic of the Congo"],
["Cote d'Ivoire"],
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
['Uganda'],
['United Republic of Tanzania'],
['Yemen'],
['Zambia'],
['Zimbabwe'],
['MijnlandAfrica']]

regio =[["Benin","Burkina Faso", "Nigeria", "Niger"],
["Burkina Faso","Mali", "Cote d'Ivoire", "Ghana", "Benin", "Niger"],
["Burundi","Democratic Republic of the Congo", "Rwanda", "United Republic of Tanzania"],
["Cameroon","Nigeria", "Chad", "Central African Republic", "Congo"],
["Central African Republic", "Congo", "Democratic Republic of the Congo", "Chad", "Sudan", "South Sudan"],
["Chad","Niger", "Nigeria", "Sudan", "Central African Republic", "Cameroon"],
["Congo","Democratic Republic of the Congo", "Cameroon", "Central African Republic"],
["Democratic Republic of the Congo","Congo", "Zambia", "Rwanda", "Burundi", "United Republic of Tanzania", "Uganda", "South Sudan", "Central African Republic"],
["Cote d'Ivoire", "Guinea", "Liberia", "Ghana", "Mali", "Burkina Faso"],
["Djibouti","Ethiopia","Yemen"],
["Egypt","Sudan"],
["El Salvador","Guatemala", "Honduras"],
["Ethiopia","Sudan", "Djibouti", "South Sudan", "Kenya"],
["Gambia","Senegal"],
["Ghana","Cote d'Ivoire", "Burkina Faso"],
["Guinea","Cote d'Ivoire", "Liberia", "Guinea-Bissau", "Senegal", "Mali"],
["Guinea-Bissau","Guinea", "Senegal"],
["Kenya", "Ethiopia", "Uganda", "United Republic of Tanzania"],
["Lesotho"],
["Liberia","Guinea", "Cote d'Ivoire"],
["Madagascar"],
["Malawi","Mozambique", "Zambia", "United Republic of Tanzania"],
["Mali","Niger", "Burkina Faso", "Cote d'Ivoire", "Mauritania", "Senegal", "Guinea"],
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
["Yemen","Djibouti"],
["Zambia","United Republic of Tanzania", "Malawi", "Mozambique", "Zimbabwe"],
["Zimbabwe", "Zambia", "Mozambique"],
["MijnlandAfrica","Benin","Burkina Faso","Burundi","Cameroon","Central African Republic","Chad","Congo","Democratic Republic of the Congo","Cote d'Ivoire","Djibouti","Egypt","Ethiopia","Gambia","Ghana","Guinea","Guinea-Bissau","Kenya","Lesotho","Liberia","Madagascar","Malawi","Mali","Mauritania","Mozambique","Niger","Nigeria","Rwanda","Senegal","South Sudan","Sudan","Swaziland",'Uganda','United Republic of Tanzania','Yemen','Zambia','Zimbabwe',]]



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
        fOut = open("Afrika_Maize.html", "a")
        f = figure(plot_width=500, plot_height=500, title=country)
        f.multi_line(xs = x_list, ys = y_list)
        html = file_html(f, CDN, "chart")
        fOut.write(html)
        fOut.close()
    else:
        continue
