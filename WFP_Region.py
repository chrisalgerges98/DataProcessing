import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

land = [["Afghanistan"],
["Armenia"],
["Bangladesh"],
["Benin"],
["Bhutan"],
["Bolivia"],
["Burkina Faso"],
["Burundi"],
["Cambodia"],
["Cameroon"],
["Central African Republic"],
["Chad"],
["Colombia"],
["Congo"],
["Democratic Republic of the Congo"],
["Costa Rica"],
["Cote d'Ivoire"], 
["Djibouti"],
["Egypt"],
["El Salvador"],
["Ethiopia"],
["Gambia"],
["Georgia"],
["Ghana"],
["Guatemala"],
["Guinea"],
["Guinea-Bissau"],
["Haiti"],
["Honduras"],
["India"],
["Indonesia"],
["Iran (Islamic Republic of)"],
["Iraq"],
["Jordan"],
["Kenya"],
["Kyrgyzstan"],
["Lao People's Democratic Republic"],
["Lebanon"],
["Lesotho"],
["Liberia"],
["Madagascar"],
["Malawi"],
["Mali"],
["Mauritania"],
["Mozambique"],
["Myanmar"],
["Nepal"],
["Niger"],
["Nigeria"],
["Pakistan"],
["Panama"],
["Peru"],
["Philippines"],
["Rwanda"],
["Senegal"],
["South Sudan"],
["Sri Lanka"],
["Sudan"],
["Swaziland"],
["Tajikistan"],
['Uganda'],
['United Republic of Tanzania'],
['Yemen'],
['Zambia'],
['Zimbabwe']]

regio = [["Afghanistan","Iran (Islamic Republic of)", "Pakistan", "Tajikistan"],
["Armenia", "Iran (Islamic Republic of)", "Georgia"],
["Bangladesh" "India", "Myanmar"],
["Benin","Burkina Faso", "Nigeria", "Niger"],
["Bhutan","India"],
["Bolivia", "Peru"],
["Burkina Faso","Mali", "Cote d'Ivoire", "Ghana", "Benin", "Niger"],
["Burundi","Democratic Republic of the Congo", "Rwanda", "United Republic of Tanzania"],
["Cambodia","Lao People's Democratic Republic"],
["Cameroon","Nigeria", "Chad", "Central African Republic", "Congo"],
["Central African Republic", "Congo", "Democratic Republic of the Congo", "Chad", "Sudan", "South Sudan"],
["Chad","Niger", "Nigeria", "Sudan", "Central African Republic", "Cameroon"],
["Colombia","Panama", "Peru"],
["Congo","Democratic Republic of the Congo", "Cameroon", "Central African Republic"],
["Democratic Republic of the Congo","Congo", "Zambia", "Rwanda", "Burundi", "United Republic of Tanzania", "Uganda", "South Sudan", "Central African Republic"],
["Costa Rica","Panama"],
["Cote d'Ivoire","Guinea", "Liberia", "Ghana", "Mali", "Burkina Faso"],
["Djibouti","Ethiopia"],
["Egypt","Sudan"],
["El Salvador","Guatemala", "Honduras"],
["Ethiopia","Sudan", "Djibouti", "South Sudan", "Kenya"],
["Gambia","Senegal"],
["Georgia","Armenia"],
["Ghana","Cote d'Ivoire", "Burkina Faso"],
["Guatemala","El Salvador", "Honduras"],
["Guinea","Cote d'Ivoire", "Liberia", "Guinea-Bissau", "Senegal", "Mali"],
["Guinea-Bissau","Guinea", "Senegal"],
["Haiti"],
["Honduras","El Salvador", "Guatemala"],
["India","Pakistan", "Nepal", "Bhutan", "Bangladesh", "Myanmar"],
["Indonesia","Philippines"],
["Iran (Islamic Republic of)","Afghanistan", "Pakistan", "Iraq", "Armenia"],
["Iraq", "Iran (Islamic Republic of)", "Jordan"],
["Jordan","Iraq"],
["Kenya", "Ethiopia", "Uganda", "United Republic of Tanzania"],
["Kyrgyzstan","Tajikistan"],
["Lao People's Democratic Republic","Cambodia", "Myanmar"],
["Lebanon"],
["Lesotho"],
["Liberia","Guinea", "Cote d'Ivoire"],
["Madagascar"],
["Malawi","Mozambique", "Zambia", "United Republic of Tanzania"],
["Mali","Niger", "Burkina Faso", "Cote d'Ivoire", "Mauritania", "Senegal", "Guinea"],
["Mauritania","Mali", "Senegal"],
["Mozambique","Malawi", "United Republic of Tanzania", "Zambia", "Swaziland", "Zimbabwe"],
["Myanmar","Lao People's Democratic Republic", "Bangladesh", "India"],
["Nepal","India"],
["Niger","Mali", "Chad", "Nigeria", "Benin", "Burkina Faso"],
["Nigeria","Cameroon", "Chad", "Niger", "Benin"],
["Pakistan","India", "Afghanistan", "Iran (Islamic Republic of)"],
["Panama","Costa Rica", "Colombia"],
["Peru","Bolivia", "Colombia"],
["Philippines", "Indonesia"],
["Rwanda","Uganda", "United Republic of Tanzania", "Burundi", "Democratic Republic of the Congo"],
["Senegal","Gambia", "Guinea", "Guinea-Bissau", "Mali", "Mauritania"],
["South Sudan","Ethiopia", "Kenya", "Uganda", "Democratic Republic of the Congo", "Central African Republic"],
["Sri Lanka"],
["Sudan","Chad", "Central African Republic", "Egypt", "Ethiopia"],
["Swaziland","Mozambique"],
["Tajikistan","Kyrgyzstan", "Afghanistan"],
["Uganda","Kenya", "South Sudan", "Democratic Republic of the Congo", "Rwanda", "United Republic of Tanzania"],
["United Republic of Tanzania","Kenya", "Uganda", "Rwanda", "Burundi", "Democratic Republic of the Congo", "Zambia", "Malawi"],
["Yemen","Djibouti"],
["Zambia","United Republic of Tanzania", "Malawi", "Mozambique", "Zimbabwe"],
["Zimbabwe", "Zambia", "Mozambique"]]



df = pd.read_csv("WFPFinal.csv")

countries = df["country"].unique()

# change to get charts about regions and certain product
product = "Cabbage"
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
        fOut = open("Cabbage_Chart.html", "a")
        f = figure(plot_width=500, plot_height=500, title=country)
        f.multi_line(xs = x_list, ys = y_list)
        html = file_html(f, CDN, "chart")
        fOut.write(html)
        fOut.close()
    else:
        continue