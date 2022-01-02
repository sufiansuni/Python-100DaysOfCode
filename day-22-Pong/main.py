from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_right = Paddle((350,0))
paddle_left = Paddle((-350,0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(paddle_right.go_up, "Up")
screen.onkeypress(paddle_right.go_down, "Down")
screen.onkeypress(paddle_left.go_up, "w")
screen.onkeypress(paddle_left.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with top/bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detect when paddle_right misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.point_left()

    # Detect when paddle_left misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.point_right()

screen.exitonclick()
