import turtle

bob = turtle.Turtle()
# bob.forward(100)
# bob.left(90)

bob.begin_fill()
bob.color("Red")
bob.forward(100)

bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.end_fill()

bob.penup()
bob.forward(200)
bob.pendown()

bob.begin_fill()
bob.color("Blue")
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.right(90)
bob.forward(100)
bob.end_fill()

bob.setheading(90)

turtle.done()
