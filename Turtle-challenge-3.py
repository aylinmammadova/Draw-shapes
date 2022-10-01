from turtle import Turtle
import random

timmy = Turtle()

# # Method 1:
for _ in range(3, 11):
    r = random.random()
    g = random.random()
    b = random.random()
    angle = 360 / _
    timmy.color(r, g, b)
    for side in range(_):
        timmy.forward(100)
        timmy.right(angle)

timmy.forward(100)

# # Method 2:
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGrey", "SeaGreen"]
#
#
# def draw_shape(sides):
#     angle = 360/sides
#     color = random.choice(colors)
#     timmy.color(color)
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for side in range(3, 11):
#     draw_shape(side)

