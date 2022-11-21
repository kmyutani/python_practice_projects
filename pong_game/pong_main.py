from turtle import Screen, Turtle
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
import time

screen = Screen()
screen.setup(1000, 600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

scoreboard = ScoreBoard()
left_paddle = Paddle((-470, 0))
right_paddle = Paddle((470, 0))
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 445 or ball.distance(left_paddle) < 50 and ball.xcor() < -445:
        ball.bounce_x()

    if ball.xcor() > 480:
        ball.reset_position()
        scoreboard.increase_score_left()

    if ball.xcor() < -480:
        ball.reset_position()
        scoreboard.increase_score_right()
screen.exitonclick()