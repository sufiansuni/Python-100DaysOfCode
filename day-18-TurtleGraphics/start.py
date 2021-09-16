from turtle import Turtle, Screen, colormode
from random import randint, choice

colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("DarkGreen")
timmy.speed(0)
timmy.up()


def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_square(turtle, length):
    for _ in range(4):
        turtle.down()
        turtle.forward(length)
        turtle.up()
        turtle.right(90)


def draw_dotted(turtle, spacing, times):
    for _ in range(times):
        turtle.down()
        turtle.forward(spacing)
        turtle.up()
        turtle.forward(spacing)


def draw_polygon(turtle, sides, length):
    turtle.pencolor(random_colour())
    turtle.down()
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(360 / sides)
    turtle.up()


def draw_random_walk(turtle, length, times):
    turtle.pensize(5)
    for _ in range(times):
        turtle.pencolor(random_colour())
        turtle.setheading(choice([0, 90, 180, 270]))
        turtle.down()
        turtle.forward(length)
        turtle.up()


def draw_spirograph(turtle, radius, tilt):
    for _ in range(int(360 / tilt)):
        turtle.pencolor(random_colour())
        turtle.down()
        turtle.circle(radius)
        turtle.up()
        turtle.right(tilt)


# draw_square(timmy, 100)
# draw_dotted(timmy, 10, 15)
# for size_input in range(3, 11):
#     draw_polygon(timmy, size_input, 50)
# draw_random_walk(timmy, 20, 50)

# draw_spirograph(timmy, 100, 5)

screen = Screen()
screen.exitonclick()
