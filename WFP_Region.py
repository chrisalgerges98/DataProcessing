import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.resources import CDN
from bokeh.embed import file_html

land = [["Afghanistan"],["Armenia"],["Bangladesh"],["Benin"],["Bhutan"],["Bolivia"],["Burkina Faso"],["Burundi"],["Cambodia"],["Cameroon"],["Central African Republic"],["Chad"],["Colombia"],["Democratic Republic of the Congo"],["Congo Brazzaville"],["Congo Kinshasa"],
["Costa Rica"],["Cote d'Ivoire"], ["Djibouti"],["Egypt"],["El Salvador"],["Ethiopia"],["Gambia"],["Georgia"],["Ghana"],["Guatemala"],["Guinea"],["Guinea-Bissau"],["Haiti"],["Honduras"],["India"],["Indonesia"],["Iran (Islamic Republic of)"],
["Iraq"],["Jordan"],["Kenya"],["Kyrgyzstan"],["Lao people's Democratic Republic"],["Lebanon"],["Lesotho"],["Liberia"],["Madagascar"],["Malawi"],["Mali"],["Mauritania"],["Mozambique"],["Myanmar"],["Nepal"],["Niger"],["Nigeria"],
["Pakistan"],["Panama"],["Peru"],["Philippines"],["Rwanda"],["Senegal"],["Somalia"],["South Sudan"],["Sri Lanka"],["Sudan"],["Swaziland"],["Tajikistan"],['Uganda'],['United Republic of Tanzania'],
['Yemen'],['Zambia'],['Zimbabwe']]

regio = [["Afghanistan","Iran (Islamic Republic of)", "Pakistan", "Tajikistan"],["Amernia" "Iran (Islamic Republic of)", "Georgia"],["Bangladesh" "India", "Myanmar"],["Benin","Burkina Faso", "Nigeria", "Niger"],["Benin","Burkina Faso", "Nigeria", "Niger"],
["Bhutan","India"],["Bolivia", "Peru"],["Burkina Faso","Mali", "Cote d'Ivoire", "Ghana", "Benin", "Niger"],["Burundi","Congo-Kinshasa", "Rwanda", "United Republic of Tanzania"],["Cambodia","Lao people's Democratic Republic"],
["Cameroon","Nigeria", "Chad", "Central African Republic", "Congo-Brazzaville"],["Chad","Niger", "Nigeria", "Sudan", "Central African Republic", "Cameroon"],
["Colombia","Panamá", "Peru"],
["Democratic Republic of the Congo","Cameroon", "Central African Republic", "Zambia", "Rwanda", "Burundi", "United Republic of Tanzania", "Uganda", "South Sudan"],
["Congo-Brazzaville","Congo-Kinshasa", "Cameroon", "Central African Republic"],
["Congo-Kinshasa","Congo-Brazzaville", "Zambia", "Rwanda", "Burundi", "United Republic of Tanzania", "Uganda", "South Sudan", "Central African Republic"],
["Costa Rica","Panamá"],
["Cote d'Ivoire","Guinea", "Liberia", "Ghana", "Mali", "Burkina Faso"],
["Djibouti","Ethiopia", "Somalia"],
["Egypt","Sudan"],
["El Salvador","Guatemala", "Honduras"],
["Ethiopia","Sudan", "Djibouti", "Somalia", "South Sudan", "Kenya"],
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
["Kenya","Somalia", "Ethiopia", "Uganda", "United Republic of Tanzania"],
["Kyrgyzstan","Tajikistan"],
["Lao people's Democratic Republic","Cambodia", "Myanmar"],
["Lebanon"],
["Lesotho"],
["Liberia","Guinea", "Cote d'Ivoire"],
["Madagascar"],
["Malawi","Mozambique", "Zambia", "United Republic of Tanzania"],
["Mali","Niger", "Burkina Faso", "Cote d'Ivoire", "Mauritania", "Senegal", "Guinea"],
["Mauritania","Mali", "Senegal"],
["Mozambique","Malawi", "United Republic of Tanzania", "Zambia", "Swaziland", "Zimbabwe"],
["Myanmar","Lao people's Democratic Republic", "Bangladesh", "India"],
["Nepal","India"],
["Niger","Mali", "Chad", "Nigeria", "Benin", "Burkina Faso"],
["Nigeria","Cameroon", "Chad", "Niger", "Benin"],
["Pakistan","India", "Afghanistan", "Iran (Islamic Republic of)"],
["Panamá","Costa Rica", "Colombia"],
["Peru","Bolivia", "Colombia"],
["Philippines;[""Indonesia"],
["Rwanda","Uganda", "United Republic of Tanzania", "Burundi", "Democratic Republic of the Congo"],
["Senegal","Gambia", "Guinea", "Guinea-Bissau", "Mali", "Mauritania"],
["Somalia","Ethiopia", "Kenya"],
["South Sudan","Ethiopia", "Kenya", "Uganda", "Democratic Republic of the Congo", "Central African Republic"],
["Sri Lanka"],
["Sudan","Chad", "Central African Republic", "Egypt", "Ethiopia"],
["Swaziland","Mozambique"],
["Tajikistan","Kyrgyzstan", "Afghanistan"],
["Uganda","Kenya", "South Sudan", "Democratic Republic of the Congo", "Rwanda", "United Republic of Tanzania"],
["United Republic of Tanzania","Kenya", "Uganda", "Rwanda", "Burundi", "Democratic Republic of the Congo", "Zambia", "Malawi"],
["Yemen","Djibouti", "Somalia"],
["Zambia","United Republic of Tanzania", "Malawi", "Mozambique", "Zimbabwe"],
["Zimbabwe", "Zambia", "Mozambique"]]


#Print till Cote d'Ivoiry but not further don't know why Probably something WFP_csv.
df = pd.read_csv("WFPCleaned.csv")
#dataset = pd.read_csv("Regions.csv", delimiter=':')

countries = df["country"].unique()
#regions = dataset["neighbours"]
#print(regions)

#for country in countries:
#fill in country for country
#country = "Benin"
#countries = dataset["neighbours"][dataset["country"] == country]
#print(countries)


    #products = df["food"][df["country"] == country].unique()
    #fill in product for product

product = "Maize"
for i, country in zip(range(len(land)), countries):
    x_list = []
    y_list = []
    if product in df["food"][(df["country"] == country)].unique():
        #print(land[i])
        for j in regio[i]:
            x = df["year"][(df["country"] == j) & (df["food"] == product)]
            #print(x)
            y = df["average_price"][(df["country"] == j) & (df["food"] == product)]
            x_list.append(x)
            y_list.append(y)
        fOut = open("testregion2.html", "a")
        f = figure(plot_width=500, plot_height=500, title=country)
        f.multi_line(xs = x_list, ys = y_list)
        html = file_html(f, CDN, "chart2")
        fOut.write(html)
        fOut.close()
    else:
        continue