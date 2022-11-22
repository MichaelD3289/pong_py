from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

RIGHT_PADDLE = (350, 0)
LEFT_PADDLE = (-350, 0)
WINNING_SCORE = 7

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
r_paddle = Paddle(RIGHT_PADDLE)
l_paddle = Paddle(LEFT_PADDLE)
ball = Ball()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_running = True
while game_is_running:
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('y')

    if ball.distance(r_paddle) < 50 and ball.xcor() > 327 or ball.distance(l_paddle) < 50 and ball.xcor() < -327:
        ball.bounce('x')

    if ball.xcor() > 390:
        scoreboard.award_point('left')
        ball.reset()
        l_paddle.reset(LEFT_PADDLE)
        r_paddle.reset(RIGHT_PADDLE)

    if ball.xcor() < -390:
        scoreboard.award_point('right')
        ball.reset()
        l_paddle.reset(LEFT_PADDLE)
        r_paddle.reset(RIGHT_PADDLE)

    if scoreboard.l_score == WINNING_SCORE:
        scoreboard.print_winner('left')
        game_is_running = False
    elif scoreboard.r_score == WINNING_SCORE:
        scoreboard.print_winner('right')
        game_is_running = False

    time.sleep(ball.move_speed)

screen.exitonclick()