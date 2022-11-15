import turtle
from turtle import Turtle, Screen
import random
timmy = Turtle()
# Turtle preset
turtle.colormode(255)
timmy.speed("fastest")

# Color pallet used in Herst painting
new_color = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# Sets the arrow to the center of the screen
timmy.penup()
timmy.hideturtle()
timmy.setheading(205)
timmy.forward(450)
timmy.setheading(0)

dots = 100
for dot_count in range(1, dots + 1):
        timmy.dot(20, random.choice(new_color))
        timmy.forward(50)

        # Creates a new row
        if dot_count % 10 == 0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)

screen = Screen()
screen.exitonclick()
