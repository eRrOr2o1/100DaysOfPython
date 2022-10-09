# Draw a spirograph
import turtle as t
import random

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_colour = (r, g, b)
    return r_colour


def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        t.speed("fastest")
        t.color(random_color())
        t.circle(180)
        t.setheading(t.heading() + size_of_gap)


draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()
