import csv

# with open("weather_data.csv") as file:
#     contents = file.readlines()
#     for line in contents:
#         data.append(line.strip())

# temperature_index = 1
#
# temperatures = []
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         if row[temperature_index] != 'temp':
#             temperatures.append(int(row[temperature_index]))
#
# print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].tolist()
# temp_sum = 0
# temp_avg = sum(temp_list) / len(temp_list)
# print(temp_avg)

# temp_avg = data["temp"].mean()
# print(temp_avg)
# print(data["temp"].max())
# print(data["temp"].min())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((9/5)*monday.temp+32)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
