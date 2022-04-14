import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_squirrels, red_squirrels, black_squirrels]
}

data = pandas.DataFrame(squirrel_dict)
data.to_csv("squirrel_color_count.csv")
