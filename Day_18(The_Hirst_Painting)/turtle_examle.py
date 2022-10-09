# Drawing different shapes
from turtle import Turtle, Screen
import random

bob = Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# bob.shape("square")
# bob.color("Red")
# bob.forward(100)
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        bob.forward(100)
        bob.right(angle)


for shape_side_n in range(3, 12):
    bob.color(random.choice(colours))
    draw_shape(shape_side_n)
screen = Screen()
screen.exitonclick()
