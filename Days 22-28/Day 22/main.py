import csv

with open("D:\\GIT\\100-days-of-python\\Days 22-29\\Day 22\\weather_data.csv") as data_file:
    #content=data_file.readlines()
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
        print(row)
    print(temperatures)
