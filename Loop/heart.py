import turtle

# Create a turtle screen and set up the window
screen = turtle.Screen()
screen.title("Heart")
screen.setup(width=400, height=400)
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()
pen.color('green')
pen.fillcolor('blue')
pen.speed(4)
pen.begin_fill()

# Draw the heart shape
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)

# Draw the other half of the heart
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)

# Fill the heart shape
pen.end_fill()

# Hide the turtle
pen.hideturtle()

# Keep the window open until closed by the user
turtle.done()
