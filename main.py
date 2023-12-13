from turtle import Turtle, Screen

# initialize object
don = Turtle()
# Change shape of cursor and it's color
don.shape("turtle")
don.color("purple4")
# # Make the turtle move to create a square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# Create a dashed line
for _ in range(20):
    don.forward(10)
    don.penup()
    don.forward(10)
    don.pendown()



# open drawing screen until its clicked
screen = Screen()
screen.exitonclick()
