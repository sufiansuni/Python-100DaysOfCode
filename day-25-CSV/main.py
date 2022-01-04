# with open("day-25-CSV/weather_data.csv") as data_file:
#     data = data_file.readlines()

# print(data)

# import csv

# temperatures = []

# with open("day-25-CSV/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas

# data variable is of type DataFrame, defined by pandas module
data = pandas.read_csv("day-25-CSV/weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# data_list = data["temp"].to_list()
# print(data_list)

# print("Average Temp: ", data["temp"].mean())
# print("Max Temp: ", data["temp"].max())

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp_F = int(monday.temp) *9/5 +32
# print(monday_temp_F)

school_data_dict = {
    "students": ["Amy", "Ben", "Charlie"],
    "scores": [76,56,69]
}

school_data = pandas.DataFrame(school_data_dict)
school_data.to_csv("day-25-CSV/school_data.csv")
