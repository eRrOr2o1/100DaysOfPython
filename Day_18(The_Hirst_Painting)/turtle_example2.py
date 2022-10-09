# Generate random walk with random colour

import turtle as b
import random

b.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    r_colour = (r, g, b)
    return r_colour


# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# "SeaGreen"]
directions = [0, 45, 90, 180, 270]
b.pensize(15)
b.speed("fastest")

for i in range(200):
    b.color(random_color())
    b.forward(50)
    b.setheading(random.choice(directions))
