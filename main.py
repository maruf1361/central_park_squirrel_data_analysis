import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
white_color_count = len(data[data["Primary Fur Color"] == "White"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "White"],
    "count": [gray_color_count, cinnamon_color_count, white_color_count]
}

df = pandas.DataFrame(data_dict)

df.to_csv("color_count.csv")
