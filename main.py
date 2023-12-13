from turtle import Turtle, Screen
import random

# initialize object
don = Turtle()
# Change shape of cursor and it's color
don.shape("turtle")
don.color("purple4")

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
# def draw_shape(number_sides):
#     angle = 360 / number_sides
#     for _ in range(number_sides):
#         don.forward(100)
#         don.right(angle)
#
# # Add a different color for each shape being drawn
colors = ["blue", "red", "SlateGray", "purple", "orange", "green", "pink", "DarkOrchid"]

# for side_num in range(3, 11):
#     don.color(random.choice(colors))
#     draw_shape(side_num)
# Create a random walk function which changes colors for each step taken, and make pen size bigger
directions = [0, 90, 180, 270]
don.pensize(15)


def random_walk(steps):
    for turn in range(steps):
        don.color(random.choice(colors))
        don.forward(30)
        don.setheading(random.choice(directions))


random_walk(200)
# open drawing screen until its clicked
screen = Screen()
screen.exitonclick()
