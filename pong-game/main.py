from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1920, height=1080)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

r_paddle = Paddle((-920, 0))
l_paddle = Paddle((920, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 480 or ball.ycor() < -480:
        ball.bounce()

    if ball.distance(r_paddle) < 30 or ball.distance(l_paddle) < 30:
        ball.paddle_hit()

    if ball.xcor() > 900 or ball.xcor() < -900:
        if ball.distance(r_paddle) < 100 or ball.distance(l_paddle) < 100:
            ball.paddle_hit()

    if ball.xcor() > 940:
        scoreboard.increase_score1()
        ball.setheading(0)
        ball.goto(0, 0)
        ball.move_speed = 0.15
    elif ball.xcor() < -940:
        scoreboard.increase_score2()
        ball.setheading(180)
        ball.goto(0, 0)
        ball.move_speed = 0.15

    if scoreboard.score1 == 10 or scoreboard.score2 == 10:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
