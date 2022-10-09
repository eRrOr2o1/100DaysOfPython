import math
import turtle

bob = turtle.Turtle()
bob.color("red", "yellow")
bob.speed(10)

# bob.begin_fill()
for i in range(100):
    bob.forward(100)
    bob.left(math.sqrt(i) * 10)
    bob.left(20)

# bob.end_fill()

turtle.done()
