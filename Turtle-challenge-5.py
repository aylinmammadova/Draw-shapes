import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
timmy.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


for angle in range(0, 361, 5):
    timmy.color(random_color())
    timmy.setheading(angle)
    timmy.circle(100)

screen = Screen()
screen.exitonclick()
