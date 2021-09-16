from turtle import Turtle, Screen, colormode
from random import choice
import colorgram

colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkGreen")
timmy.speed(0)
timmy.up()
timmy.hideturtle()


def extract_colours(file, color_amount):
    extracted_colors = colorgram.extract(file, color_amount)
    rgb_colors = []

    for color in extracted_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)

    return rgb_colors


colors = extract_colours("source.jpg", 25)
number_of_dots = 100
timmy.setpos(-250, -250)

for dot in range(1, number_of_dots+1):
    random_color = choice(colors)
    timmy.down()
    timmy.dot(20, random_color)
    timmy.up()

    if dot % 10 != 0:
        timmy.forward(50)
    else:
        timmy.setpos(-250, -250 + (50 * dot / 10))

screen = Screen()
screen.exitonclick()
