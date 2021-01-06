from turtle import Screen, Turtle
from paddles import Paddles
from pong_screen import PongScreen

scr = PongScreen()
paddles = Paddles()
scr.screen.update()


scr.screen.listen()

game_over = False

while not game_over:
    # Right paddle motion
    scr.screen.onkey(paddles.right_up, "Up")
    scr.screen.onkey(paddles.right_down, "Down")
    # Left paddle motion
    scr.screen.onkey(paddles.left_up, "w")
    scr.screen.onkey(paddles.left_down, "s")
    scr.screen.update()


scr.screen.exitonclick()


