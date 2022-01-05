import pandas

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

print(weather_c)

weather_dataframe = pandas.DataFrame(weather_c.items())

print(weather_dataframe)
for (index, row) in weather_dataframe.iterrows():
    print(row)
