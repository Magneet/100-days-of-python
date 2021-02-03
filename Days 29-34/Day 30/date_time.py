import datetime as dt

print(dt.datetime.now())

file="Template_processes20-10-2020-18-55-25-4096.csv"
f = file[18:-9]
dt_obj = dt.datetime.strptime(f, "%d-%m-%Y-%H-%M-%S")

print(dt_obj)