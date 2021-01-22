import turtle as t
import random
screen = t.Screen()
t.colormode(255)
turtles=["red","green","blue","purple","yellow","brown"]
y_pos = [-70, -40, -10, 20, 50, 80]
screen.setup(width=500,height=400)
bet = screen.textinput(title="Make your bet", prompt="Who's going to win?")
is_race_on = False

all_turtles=[]

for turtle_index in range(0,6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(turtles[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230 and is_race_on == True:
            winner = turtle.pencolor()
            if winner == bet:
                print(f"The winner is {winner} you won")
            else:
                print(f"The winner is {winner} you lost")
            is_race_on = False
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)











def random_color():
    r = random.randint(2, 255)
    g = random.randint(2, 255)
    b = random.randint(2, 255)
    random_color = (r, g, b)
    return random_color




screen.exitonclick()