from turtle import Screen, Turtle
from paddle import Paddle
from pong_screen import PongScreen

scr = PongScreen()
right_paddle = Paddle((450, 0))
left_paddle = Paddle((-450, 0))
scr.screen.update()


scr.screen.listen()

game_over = False

while not game_over:
    # Left paddle motion
    scr.screen.onkey(left_paddle.up, "w")
    scr.screen.onkey(left_paddle.down, "s")
    # Right paddle motion

    scr.screen.onkey(right_paddle.up, "Up")
    scr.screen.onkey(right_paddle.down, "Down")
    scr.screen.update()


scr.screen.exitonclick()


