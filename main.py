from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

RIGHT_PADDLE = (350, 0)
LEFT_PADDLE = (-350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)
screen.listen()

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
    time.sleep(0.1)

screen.exitonclick()