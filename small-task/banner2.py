import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Banner")
screen.bgcolor("lightblue")

# Draw the banner
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(-200, 50)
pen.pendown()
pen.fillcolor("white")
pen.begin_fill()
for _ in range(2):
    pen.forward(400)
    pen.right(90)
    pen.forward(100)
    pen.right(90)
pen.end_fill()

# Add text
pen.penup()
pen.goto(-180, 20)
pen.color("black")
pen.write("Welcome!", font=("Arial", 24, "bold"))

# Keep the window open
turtle.done()
