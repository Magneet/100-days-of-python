import turtle as t
import random

t.colormode(255)

tim = t.Turtle()
screen = t.Screen()

def move_forwards():
    tim.color(random_color())
    tim.forward(10)

def move_backwards():
    tim.color(random_color())
    tim.backward(10)

def turn_left():
    tim.color(random_color())
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    tim.color(random_color())
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()


def random_color():
    r = random.randint(2, 255)
    g = random.randint(2, 255)
    b = random.randint(2, 255)
    random_color = (r, g, b)
    return random_color

screen.listen()

screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear_screen,"c")

screen.exitonclick()