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

ListofProducts = ["Beans (white)","Cassava meal (gari)","Maize","Maize (white)","Millet","Rice (imported)","Sorghum","Beans (niebe)",
"Beans","Cassava flour","Rice (low quality, local)","Sweet potatoes","Cassava (cossette)","Groundnuts (shelled)","Onions","Peas (yellow)",
"Rice (local)","Sesame","Sorghum (red)","Sorghum (white)","Rice","Wheat flour","Cassava (fresh)","Fish (smoked)","Meat (beef)",
"Meat (chicken, frozen)","Oil (palm)","Rice (mixed, low quality)","Cassava","Cassava (chikwangue)","Fish (fresh)","Fish (salted)",
"Fuel (diesel)","Maize flour","Maize meal","Meat (chicken)","Meat (goat, with bones)","Plantains","Salt","Sugar","Bread","Fuel (kerosene)",
"Oil (vegetable)","Pasta","Beans (fava, dry)","Garlic","Ghee (artificial)","Ghee (natural)","Lentils","Oil (maize)","Onions (red)","Onions (white)",
"Potatoes","Tomatoes","Wheat","Groundnuts (unshelled)","Maize (local)","Rice (long grain, imported)","Rice (medium grain, imported)",
"Rice (paddy, long grain, local)","Rice (small grain, imported)","Plantains (apentu)","Yam","Fonio","Oil (vegetable, imported)","Cocoa",
"Cornstarch","Fish (appolo)","Fish (dry)","Peanut","Rice (denikassia, imported)","Yam (florido)","Beans (dry)","Milk (cow, pasteurized)",
"Potatoes (Irish)","Beans (sugar-red)","Bread (brown)","Oil (sunflower)","Peas (split, dry)","Cowpeas","Fuel (petrol-gasoline)",
"Rice (white, imported)","Rice (paddy)","Sorghum (taghalit)","Groundnuts (large, shelled)","Groundnuts (Mix)","Groundnuts (small, shelled)",
"Maize meal (white, first grade)","Maize meal (white, with bran)","Oil (vegetable, local)","Sugar (brown, local)","Wheat flour (local)",
"Bananas","Beans (green, fresh)","Charcoal","Eggplants","Guava","Livestock (Goat)","Livestock (Sheep)","Mangoes","Meat (goat)","Papaya",
"Passion fruit","Peas (fresh)","Peppers (green)","Rice (imported, Tanzanian)","Sorghum flour","Spinach","Zucchini","Maize (imported)",
"Beans (red)","Millet (white)","Sorghum (food aid)","Beans (sugar)","Sugar (brown)","Beans (kidney red)","Eggs","Peas (yellow, split)",
"Cassava meal","Maize meal (white, breakfast)","Maize meal (white, roller)"] # OOK HIERZO

df = pd.read_csv("WFPAfricaFinal.csv")

countries = df["country"].unique()

# change to get charts about regions and certain product
for product in ListofProducts = 
    for i, country in zip(range(len(land)), countries):
        x_list = []
        y_list = []
        if product in df["food"][(df["country"] == country)].unique():
            print(land[i])
            print(i)
            for j in regio[i]:
                print(j)
                x = df["year"][(df["country"] == j) & (df["food"] == product)]
                print(x)
                y = df["price_per_unit"][(df["country"] == j) & (df["food"] == product)]
                x_list.append(x)
                y_list.append(y)
            fOut = open("Afrika_Per_Product.html", "a")
            f = figure(plot_width=500, plot_height=500, title=country)
            f.multi_line(xs = x_list, ys = y_list)
            html = file_html(f, CDN, "chart")
            fOut.write(html)
            fOut.close()
        else:
            continue
