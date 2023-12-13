from turtle import Turtle, Screen
import random

# initialize object
don = Turtle()
# Change shape of cursor and it's color
don.shape("turtle")
don.color("purple4")
colors = ["blue", "red", "yellow", "purple", "orange", "green", "pink", "DarkOrchid"]


# # Make the turtle move to create a square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
# # Create a dashed line
# for _ in range(20):
#     don.forward(10)
#     don.penup()
#     don.forward(10)
#     don.pendown()
# Draw two a square and a pentagon define angle degrees by dividing 360 / number of sides
# square_angle = 360/4
# pentagon_angle = 360/5
# for _ in range(4):
#     don.forward(20)
#     don.right(square_angle)
#
# for _ in range(5):
#     don.forward(20)
#     don.right(pentagon_angle)
# Create a function to draw shapes
def draw_shape(number_sides):
    angle = 360 / number_sides
    for _ in range(number_sides):
        don.forward(100)
        don.right(angle)


for side_num in range(3, 11):
    don.color(random.choice(colors))
    draw_shape(side_num)


# open drawing screen until its clicked
screen = Screen()
screen.exitonclick()
