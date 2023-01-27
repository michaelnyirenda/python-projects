# import csv

# with open("weather_data.csv") as csvfile:
#     weather_data = csv.reader(csvfile)
#     temperature = []
#     for row in weather_data:
#         if row[1].isnumeric():
#             temperature.append(int(row[1]))
        
#     print(temperature)    

import pandas 
import numpy as np

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# temp_average = np.mean(temp_list)
# print(temp_average)

# temp_average = data["temp"].mean()
# print(temp_average)

# print(data["temp"].max())

# print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
monday_temp_C = int(monday.temp)
monday_temp_F = monday_temp_C * 9/5 + 32
print(monday_temp_F)


