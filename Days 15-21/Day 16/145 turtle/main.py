# from turtle import Turtle, Screen

# henk = Turtle()
# henk.shape("turtle")
# henk.color("blue")
# henk.resizemode("user")
# henk.turtlesize(10,10,15)
# henk.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu"])
table.add_column("type",["Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])
table.align = "l"
print(table)
