import pandas

squirrel_data_path = "day-25-SquirrelData/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

squirrel_data = pandas.read_csv(squirrel_data_path)

fur_colors = squirrel_data["Primary Fur Color"].unique().tolist()[1:]

counts = []
for color in fur_colors:
    colored_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == color]
    counts.append(len(colored_squirrels))

squirrel_count_dict = {
    "Fur Color" : fur_colors,
    "Count" : counts
}

squirrel_count_data = pandas.DataFrame(squirrel_count_dict)
squirrel_count_data.to_csv("day-25-SquirrelData\squirrel_count.csv")
