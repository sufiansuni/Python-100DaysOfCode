from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.title("Turtle Race!")
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a colour: ")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
turtles = []
y_initial = -130
y_offset = 0

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_initial + y_offset)
    turtles.append(new_turtle)
    y_offset += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_dist = randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() >= 225:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner!")
            else:
                print(f"You've lost! The {win_color} turtle is the winner!")
            break


screen.exitonclick()

# Future Work: Finish Line, More Fair Race (Currently first created turtle has slight advantage)
