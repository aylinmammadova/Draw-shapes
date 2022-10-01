import turtle
from turtle import Turtle
import random

timmy = Turtle()
timmy.width(15)
timmy.speed(0)
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


for _ in range(200):
    angle = random.randint(0, 3)*90
    timmy.color(random_color())
    timmy.seth(angle)
    timmy.forward(30)



