from turtle import Screen, Turtle
import time
from ball import Ball
from paddle import Paddle
from pong_screen import PongScreen

scr = PongScreen()
right_paddle = Paddle((450, 0))
left_paddle = Paddle((-450, 0))
ball = Ball()
scr.screen.update()


scr.screen.listen()

game_over = False

while not game_over:
    # Move ball
    ball.move()

    # if ball touches ceiling or floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_motion *= -1

    # if ball touches paddles
    if ball.distance(right_paddle) < 35 or ball.distance(left_paddle) < 35:
        ball.x_motion *= -1

    # Left paddle motion
    scr.screen.onkey(left_paddle.up, "w")
    scr.screen.onkey(left_paddle.down, "s")

    # Right paddle motion
    scr.screen.onkey(right_paddle.up, "Up")
    scr.screen.onkey(right_paddle.down, "Down")

    scr.screen.update()


scr.screen.exitonclick()


