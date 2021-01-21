import turtle as t
import random

t.colormode(255)

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("green")
timmy.speed(100)




def random_color():
    r = random.randint(2, 255)
    g = random.randint(2, 255)
    b = random.randint(2, 255)
    random_color = (r, g, b)
    return random_color

def draw_spiro(gapsize):
    for _ in range(int(360 / gapsize)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + gapsize)
        timmy.tilt(current_heading + gapsize)
        timmy.tiltangle()

draw_spiro(3)





screen = t.Screen()


screen.exitonclick()