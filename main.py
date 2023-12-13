from turtle import Turtle, Screen

# initialize object
timmy_the_turtle = Turtle()
# Change shape of cursor and it's color
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("purple4")
# Make the turtle move to create a square
for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

# open drawing screen until its clicked
screen = Screen()
screen.exitonclick()
