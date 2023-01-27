# import csv

# with open("weather_data.csv") as csvfile:
#     weather_data = csv.reader(csvfile)
#     temperature = []
#     for row in weather_data:
#         if row[1].isnumeric():
#             temperature.append(int(row[1]))
        
#     print(temperature)    

import pandas 

data = pandas.read_csv("weather_data.csv")
print(data)