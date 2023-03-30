

# with open("weather_data.csv") as data_files:
#     data = data_files.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_files:
#     data = csv.reader(data_files)
#     temperature = []
#     for row in data: 
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas 
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# data_dict = data.to_dict()
# print(data_dict)
# print(data["temp"])

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# print(data["temp"].mean())
# print(data["temp"].max())

#Get Data in Columns
# print(data.condition)

#Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# # print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

#Create a dataFrame from scratch 
# data_dict = {
#     "Student": ["Anuraj", "Aditya", "Rohan"],
#     "Scores": [80, 90, 50]
# }
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)


data_dict= {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

dp = pandas.DataFrame(data_dict)
dp.to_csv("Squirrel.csv")