import pandas

data = pandas.read_csv("D:\\GIT\\100-days-of-python\\Days 22-29\\Day 22\\weather_data.csv")

def average(lst): 
    return sum(lst) / len(lst) 

#data = pandas.read_csv("D:\\GIT\\100-days-of-python\\Days 22-29\\Day 22\\CUMONITOR01.controlUp.demo-ControlUp_Machines_09_28_2020_08_10_56.csv", skiprows=[0] , header=[0])
temp_list = data["temp"].to_list()
print(average(temp_list))
print(data["temp"].quantile(q=0.9))
print(data["temp"].max())
print(data.day)