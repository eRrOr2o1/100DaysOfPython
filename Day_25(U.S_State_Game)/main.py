# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv

# with open("weather_data.csv") as data_files:
#     data = csv.reader(data_files)  # Read csv file
#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data)) # DataFrame type as it's a 2 Dimensional Data Structure
# print(type(data["temp"]))  # Series type as it's a 1 Dimensional Data Structure
# data_dict = data.to_dict()
# print(data_dict)  # Converting data to dictonary
#
# data_list = data["temp"].max()
# print(data_list)  # Converting data to dictonary
#
# # Get data in coloumn
# # print(data["condition"])
# print(data.condition)

# Get data in row
# print(data[data.day == "Monday"])

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# table = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(table)


#  The Great Squirrel Census Data Analysis (with Pandas!)
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)